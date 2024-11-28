from models.teetime import TeeTime
from repositories.teetime_repository import TeeTimeRepository

class TeeTimes:
    @staticmethod
    def create_teetime(data):
        if data['type'] == 'Regular':
            teetime = TeeTime(
                start_date=data['startDate'],
                player_count=data['playerCount'],
                type=data['type'],
                member_id=data['memberId']
            )
        elif data['type'] == 'Standing':
            teetime = TeeTime(
                start_date=data['startDate'],
                end_date=data.get('endDate', None),
                requested_day=data['requestedDay'],
                requested_time=data['requestedTime'],
                member_list=data['memberList'],
                type=data['type'],
                member_id=data['memberId']
            )
        else:
            raise ValueError('Invalid type of tee time.')

        # Save the tee time using repository layer
        TeeTimeRepository.create_teetime(teetime)
        return True

    @staticmethod
    def get_teetime(teetime_id):
        return TeeTimeRepository.get_teetime(teetime_id)

    @staticmethod
    def find_teetime():
        return TeeTimeRepository.find_teetime()