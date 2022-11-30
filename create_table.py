import psycopg2
# from config import config


def create_tables():
	""" create tables in the PostgreSQL database"""
	commands = (
		"""
		CREATE TABLE student (
			student_id SERIAL PRIMARY KEY,
			student_name VARCHAR(255) NOT NULL
		)
		""",
		""" CREATE TABLE grade (
				grade_id SERIAL PRIMARY KEY,
				grade_name VARCHAR(255) NOT NULL
				)
		""")
	conn = None
	try:
		# read the connection parameters
		# params = config()
		# connect to the PostgreSQL server
		conn = psycopg2.connect("postgresql://test_db_uodg_user:xLjrLk3HhNOZSdn2DZa2jFznzRqEfxO5@dpg-ce3cl3la4999gmei5i9g-a.oregon-postgres.render.com/test_db_uodg")
		cur = conn.cursor()
		# create table one by one
		for command in commands:
			cur.execute(command)
		# close communication with the PostgreSQL database server
		cur.close()
		# commit the changes
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


# if __name__ == '__main__':
# 	create_tables()
