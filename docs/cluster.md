
# Data layout on Sherlock

The stacks data on Sherlock sits in two places. First, the source code is deployed to the lab's shared home directory:

`/share/PI/malgeehe/code/stacks`

And, the data sits on the scratch disk:

`/scratch/PI/malgeehe/data/stacks`

The data directory looks like this:

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

The `dist`, `raw`, and `ext` directories each store copies of the corpora, formatted in different ways:

- **`dist`** - A staging area for the raw transmission data that gets moved onto the cluster - generally tarballs and zipfiles that get transferred with `scp`. This is the most "upstream" version of the data, identical to the original format that we received.

- **`raw`** - The raw files that the extraction jobs run against. In most cases, these are just decompressed copies of the bundles in `dist` without any changes, but in a couple of cases there are some small changes that need to be made before the jobs can run. Eg, in the Price Lab corpus, there's a zipfile embedded in the original bundle that has to get opened up. The final formats expected by the adapters are documented by the stacks-fixtures repository, which contains the testing data that the test suite runs against. As long as the data in `raw` looks the same, the adapters will work as expected.

- **`ext`** - The output of the extraction jobs. These are the final, normalized versions of the texts that we can run code against. Each of the top-level corpus directories in `raw` gets mirrored in `ext` - eg, texts pulled from `raw/ecco` get written into `ext/ecco`. Inside of the `ext` folders, the texts are stored as bzipped JSON files, laid out in a hash-based directory structure based on the identifiers of the texts in the original corpora.

For example,


in a directory structure that's designed to (a) prevent texts form accidentally getting dupliced by multiple runs of the same extraction job and (b) avoid huge directories with millions of files that break `ls`.
