from flask import g


class Entity:
    def __init__(self, name, coordinate, labels):
        self.name = name
        self.coordinate = coordinate
        self.labels = labels


def create_entity(name, coordinate, labels):
    entity = Entity(name, coordinate, labels)
    g.db.execute('INSERT INTO entities VALUES (?, ?, ?)', (entity.name, entity.coordinate, entity.labels))
    g.db.commit()


def get_entity(name):
    cur = g.db.execute('SELECT * FROM entities WHERE name = ?', (name,))
    row = cur.fetchone()
    if row is not None:
        return Entity(row[0], row[1], row[2])
    else:
        return None


def update_entity(name, new_coordinate, new_labels):
    g.db.execute('UPDATE entities SET coordinate =?, labels =? WHERE name = ?', (new_coordinate, new_labels, name))
    g.db.commit()


def delete_entity(name):
    g.db.execute('DELETE FROM entities WHERE name = ?', (name,))
    g.db.commit()


def get_all_entities():
    cur = g.db.execute('SELECT * FROM entities')
    rows = cur.fetchall()
    return [Entity(row[0], row[1], row[2]) for row in rows]


def filter_entities(label):
    cur = g.db.execute('SELECT * FROM entities WHERE labels LIKE ?', ('%' + label + '%',))
    rows = cur.fetchall()
    return [Entity(row[0], row[1], row[2]) for row in rows]


def get_coordinates():
    cur = g.db.execute('SELECT coordinate FROM entities')
    rows = cur.fetchall()
    coordinates = [tuple(map(int, coord[0].split(','))) for coord in rows]
    return coordinates
