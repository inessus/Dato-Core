'''
Copyright (C) 2015 Dato, Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import graphlab as gl
import graphlab.connect as _mt

def connect_odbc(conn_str):
    """
    Create a stateful connection with a database.

    An ODBC driver manager program (unixODBC) must be installed with one or
    more functional drivers in order to use this feature.  Please see the `User Guide 
    <https://dato.com/learn/userguide/index.html#ODBC_Integration>`_
    for more details.

    Parameters
    ----------
    conn_str : str
        A standard ODBC connection string.

    Returns
    -------
    out : graphlab.extensions._odbc_connection.unity_odbc_connection

    Examples
    --------
    >>> db = graphlab.connect_odbc("DSN=my_awesome_dsn;UID=user;PWD=mypassword")
    """
    db = gl.extensions._odbc_connection.unity_odbc_connection()
    db._construct_from_odbc_conn_str(conn_str)
    _mt._get_metric_tracker().track('connect_odbc', properties={'dbms_name':db.dbms_name,'dbms_version':db.dbms_version})
    return db

def set_libodbc_path(path):
    """
    Set the first path that GraphLab Create will search for libodbc.so.

    Since ODBC requires a driver manager to be installed system-wide, we
    provide this to help you if it is installed in a non-standard location.
    GraphLab Create will also search on the system's default library paths, so
    if you installed your driver manager in a standard way, you shouldn't need
    to worry about this function.
    """
    gl.set_runtime_config('GRAPHLAB_LIBODBC_PREFIX', path)

def get_libodbc_path():
    """
    Get the first path that GraphLab Create will search for libodbc.so.
    """
    c = gl.get_runtime_config()
    return c['GRAPHLAB_LIBODBC_PREFIX']
