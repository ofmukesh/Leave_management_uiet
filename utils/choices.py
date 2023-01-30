class FieldChoices():
    def genderChoices():
        return ([
            ('Male', 'Male'),
            ('Female', 'Female'),
        ])

    def titleChoices():
        return ([
            ('Mr.', 'Mr.'),
            ('Ms.', 'Ms.'),
            ('Dr.', 'Dr.'),
            ('Prof.', 'Prof.'),
        ])

    def branchChoices():
        return ([
            ('CSE', 'CSE'),
            ('Civil', 'Civil'),
            ('Mechanical', 'Mechanical'),
            ('Electrical', 'Electrical'),
            ('Boitechnology', 'Boitechnology'),
            ('Electronics', 'Electronics'),
            ('other', 'other'),
        ])

    def designationChoices():
        return ([
            ('Teaching', 'Teaching'),
            ('Non-Teaching', 'Non-Teaching'),
            ('Guest Faculty', 'Guest Faculty'),
        ])

    def timePeriodChoices():
        return ([
                ('Before-noon', 'Before-noon'),
                ('After-noon', 'After-noon'),
                ('Day', 'Day'),
                ])

    def leaveStatusChoices():
        return ([
                ('Approved', 'Approved'),
                ('Rejected', 'Rejected'),
                ('Cancelled', 'Cancelled'),
                ('Pending', 'Pending'),
                ])
