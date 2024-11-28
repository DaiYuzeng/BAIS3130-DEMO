class TeeTime:
    def __init__(self, start_date, end_date=None, requested_day=None, requested_time=None, player_count=0, member_list=None, status="Initial", type=None, priority=0, teetime_id = None, member_id=None):
        self.teetime_id = teetime_id
        self.start_date = start_date
        self.end_date = end_date
        self.requested_day = requested_day
        self.requested_time = requested_time
        self.player_count = player_count
        self.member_list = member_list or []
        self.status = status
        self.type = type
        self.priority = priority
        self.member_id = member_id