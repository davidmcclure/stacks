
# Directory layout

The stacks data on Sherlock sits in two places. First, the source code is deployed to the lab's shared home directory:

`/share/PI/malgeehe/code/stacks`

And, the data sits on the scratch disk:

`/scratch/PI/malgeehe/data/stacks`

The data directory looks like this:

```
├── metadata.db
├── dist
│   ├── bpo.tar.gz
│   ├── chicago.tar.gz
│   └── ...
├── raw
│   ├── bpo
│   ├── chicago
│   └── ...
└── ext
    ├── bpo
    ├── chicago
    └── ...
```

The `dist`, `raw`, and `ext` directories each store copies of the corpora, formatted in different ways:

- **`dist/`** - A staging area for the raw transmission data that gets moved onto the cluster - generally tarballs and zipfiles that get transferred with `scp`. This is the most "upstream" version of the data, identical to the original format that we received.

- **`raw/`** - The raw files that the extraction jobs run against. In most cases, these are just decompressed copies of the bundles in `dist` without any changes, but in a couple of cases there are some small changes that need to be made before the jobs can run. Eg, in the Price Lab corpus, there's a zipfile embedded in the original bundle that has to get opened up. The final formats expected by the adapters are documented by the stacks-fixtures repository, which contains the testing data that the test suite runs against. As long as the data in `raw` looks the same, the adapters will work as expected.

- **`ext/`** - The output of the extraction jobs. These are the final, normalized versions of the texts that we can run code against. Each of the top-level corpus directories in `raw` gets mirrored in `ext` - eg, texts pulled from `raw/ecco` get written into `ext/ecco`. Inside of the `ext` folders, the texts are stored as bzipped JSON files, laid out in a hashed directory structure that based on the identifiers of the texts in the original corpora.

  For example, say there's a text in `ncco` with the identifier of `NCCOF0092-C00000-B0005704`. The extractor will take the MD5 checksum of the identifier - in this case `f98c604e2ad64e2ccb3eefc1ce1286df` - and use the first three digits to create a directory for the file in the corresponding `ext` directory for the corpus - `ext/ncco/f98`. Then, the normalized JSON file is named from the other 29 digits in the hash. So, the final path would be `ext/ncco/f98/c604e2ad64e2ccb3eefc1ce1286df.json.bz2`.

  Since the first three digits of the checksums will be distributed (more or less) evenly from `000` -> `fff`, this basically just guarantees that the files are always split into 4096 evenly-sized segments, which keeps the filesystem nice and balanced. And, since the paths are derived from the original identifiers, there's no risk that multiple extraction runs might accidentally write duplicate versions of the same text into the repository.

# JSON format

During the extraction jobs, the adapters map the texts into a common JSON format. Right now, this looks like:

```python
{

  # The slug for the source corpus.
  'corpus': 'litlab-c20',

  # The originial identifier for the text.
  'identifier': 'hemingway-ernest-for-whom-the-bell-tolls',

  # The git commit hash of the Stacks code that wrote the file.
  'version': '428f6b1',

  # The date the file was written.
  'created_at': '2016-08-19T14:38:18.681740',

  'title': 'For Whom the Bell Tolls',
  'author_first': 'Ernest',
  'author_full': 'Hemingway, Ernest',
  'author_last': 'Hemingway',
  'year': 1940,

  # Extracted plain text.
  'plain_text': 'He lay flat on the brown, pine-needled floor of the forest...'

}
```
