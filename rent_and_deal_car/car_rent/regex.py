from django.core.validators import RegexValidator

branch_phone_regex = RegexValidator(regex=r'(^[+]\d+(?:[ ]\d+)*)',
                                    message="Phone number must be entered in the format: '+00 000 000 000'. Up to 11 "
                                            "digits allowed.")


phone_regex = RegexValidator(regex=r'(^[+]\d+(?:[ ]\d+)*)', message="Phone nr must be entered in the format: "
                                                                    "+00 000 000 000'. Up to 11 digits allowed.")