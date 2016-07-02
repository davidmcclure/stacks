

import os

from stacks.manager import app


app.run(
    debug=True,
    port=int(os.getenv('PORT', 5000)),
    host='0.0.0.0',
)
