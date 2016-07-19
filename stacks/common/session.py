

from contextlib import contextmanager

from sqlalchemy.orm import Session as BaseSession


class Session(BaseSession):

    @contextmanager
    def atomic(self):

        """
        Wrap a block in a transaction.
        """

        try:
            yield
            self.commit()

        except:
            self.rollback()
            raise

        finally:
            self.close()
