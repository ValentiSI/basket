from simple_sqlite_orm import Table, column_types


class User(Table):
    id = column_types.IdColumn()
    name = column_types.TextColumn()
    email = column_types.TextColumn()
    