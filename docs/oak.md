
# Oak archive

As of 10/22/17, all data on the scratch disk has been backed up on Oak. Ideally, we'd be able to just copy the data over as-is, but, since we've got a 1.5M-file quota on Oak - and 16M files on scratch - we had to package up the data as a collection of tar archives, which vastly reduces the file count on Oak.

Generally, top-level directories on scratch were backed up as separate archives. The original data looks like this:

```
/scratch/PI/malgeehe/data

├── ecco
├── fanfic
├── hist-vec
├── hol
├── lint
├── lint-spark
├── quotes
├── ryan
├── stacks
└── word2vec
```

And, the archived data in `/oak/stanford/groups/malgeehe` looks like:

```
/oak/stanford/groups/malgeehe

├── ecco.tar
├── fanfic.tar
├── hist-vec.tar
├── hol.tar
├── lint-spark.tar
├── lint.tar
├── quotes.tar
├── ryan.tar
├── stacks
└── word2vec.tar
```

Where each `.tar` file on Oak corresponds to one of the top-level directories on scratch. Eg, `quotes.tar` on Oak contains all of the data in the `quotes` directory on scratch.

The one big exception is the `stacks` directory, which contained all of the corpus manager data. This is by far the largest dataset, both in terms of total disk size and file count. This proved to be difficult to archive (the job would take days to run), and, even if we could do it, it's not super convenient to have all of the corpora wrapped up in a single archive, since expanding the archive back onto Sherlock would take just as long, and it would be wasteful to have to unpack everything just to get access to one or two corpora.

Instead, I archived the individual sub-directories under `stacks` separately. On scratch, the data consisted of:

```
/scratch/PI/malgeehe/data/stacks

├── backups
├── dist
├── ext
├── metadata.db
└── raw
```

Where `dist` contains the raw, tarballed transmission data for each corpus, `raw` contains the unpacked, original copies of the corpora, and `ext` is the normalized data produced by the corpus manager.

Each of these directories was archived separately under `/oak/stanford/groups/malgeehe/stacks`. Additionally, each of the corpus directories under `raw` - the original, canonical versions of each corpus - were also archived separately, to make it very easy to get access each individual corpus. On Oak:

```
/oak/stanford/groups/malgeehe/stacks

├── backups.tar
├── dist.tar
├── ext.tar
├── metadata.db
├── raw
│   ├── amfic.tar
│   ├── bpo.tar
│   ├── bpo-zip.tar
│   ├── chadh-drama.tar
│   ├── chadh-fiction.tar
│   ├── chadh-poetry.tar
│   ├── chicago.tar
│   ├── dime-westerns.tar
│   ├── ecco.tar
│   ├── eebo.tar
│   ├── litlab-c20.tar
│   ├── litlab-suspense.tar
│   ├── ncco.tar
│   └── price-lab.tar
└── raw.tar
```
