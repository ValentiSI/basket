from db import DB


def main():
    db_context = DB()

    db_context.users.insert(
        db_context.users.model(
            None,
            'Vlad',
            'a@a.com'
        )
    )

    print(*db_context.users.getAll())


if __name__ == '__main__':
    main()
