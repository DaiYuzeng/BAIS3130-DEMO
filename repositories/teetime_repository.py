from db_connection import get_db_connection

class TeeTimeRepository:
    @staticmethod
    def create_teetime(teetime):
        conn = get_db_connection()
        cursor = conn.cursor()
        if teetime.type == "Regular":
            sql = """
                INSERT INTO TeeTime (StartDate, Type, PlayerCount, MemberId, Status)
                VALUES (?, ?, ?, ?, ?)
            """
            values = (teetime.start_date, teetime.type, teetime.player_count, teetime.member_id, teetime.status)

        elif teetime.type == "Standing":
            sql = """
                INSERT INTO TeeTime (StartDate, EndDate, RequestedDay, RequestedTime, MemberList, Status, Type, Priority, MemberId)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            member_list_str = ', '.join(teetime.member_list)  # Convert member list to string
            values = (teetime.start_date, teetime.end_date, teetime.requested_day,
                      teetime.requested_time, member_list_str, teetime.status, teetime.type, teetime.priority, teetime.member_id)

        try:
            cursor.execute(sql, values)
            conn.commit()
        except Exception as e:
            raise Exception(f"Database Error: {str(e)}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def find_teetime():
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            sql = 'SELECT * FROM TeeTime'
            cursor.execute(sql)
            teetimes = cursor.fetchall()
            return [dict(zip([column[0] for column in cursor.description], row)) for row in teetimes]
        except Exception as e:
            raise Exception(f"Database Error: {str(e)}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_teetime(teetime_id):
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            sql = 'SELECT * FROM TeeTime WHERE TeeTimeId LIKE %?%'
            cursor.execute(sql, (teetime_id,))
            teetime = cursor.fetchone()
            return teetime
        except Exception as e:
            raise Exception(f"Database Error: {str(e)}")
        finally:
            cursor.close()
            conn.close()