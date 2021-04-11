from py2cozy import config

import json
import subprocess as sp
import pandas as pd

def ls_recent(n=5):
    ls_files = sp.run(['ACH', 'export', 'io.cozy.files', '-u', config.URL], stdout=sp.PIPE)
    ls_files = json.loads(ls_files.stdout)
    ls_files = pd.DataFrame(ls_files['io.cozy.files'])
    ls_files.created_at = pd.to_datetime(ls_files.created_at)
    out = ls_files.sort_values('created_at', ascending=False).head(n=n).loc[:,['name', 'created_at']]
    _ = out.apply(lambda line : print("{}/{}/{} - {}".format(line.iloc[1].year, 
                                                             line.iloc[1].month,
                                                             line.iloc[1].day,
                                                             line.iloc[0])), axis=1)