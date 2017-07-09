

import attr
import os


@attr.s
class Corpus:

    path = attr.ib()

    def flush_row(self, row):
        """Dump db rows + (annotated) text.
        """
        corpus = getattr(row, 'corpus', None)
        text_hash = getattr(row, 'text_hash', None)

        if not corpus or not text_hash:
            return

        prefix = text_hash[:3]
        suffix = text_hash[3:]

        path = os.path.join(self.path, corpus, prefix, suffix)

        return path
