#!/usr/bin/env python


from stacks.corpus import Corpus


if __name__ == '__main__':
    Corpus.from_env().load_db()
