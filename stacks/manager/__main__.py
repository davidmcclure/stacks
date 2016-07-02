

import os

from . import app


app.run(
    port=os.getenv('PORT', 5000),
    host='0.0.0.0',
)
