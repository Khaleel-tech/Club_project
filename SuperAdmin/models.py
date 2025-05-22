from django.db import models

# Create your models here.

from django.db import models


#students model
class Student(models.Model):
    
    Branch_choices = [
        ("", "Select Branch"),
        ("B.Com", "B.Com"),
        ("B.A", "B.A"),
        ("B.Arch", "B.Arch"),
        ("B.Com.(Hons)", "B.Com.(Hons)"),
        ("B.Pharmacy", "B.Pharmacy"),
        ("B.Sc - VC", "B.Sc - VC"),
        ("B.Sc (Animation & Gaming)", "B.Sc (Animation & Gaming)"),
        ("B.Sc (Hons.) Agriculture", "B.Sc (Hons.) Agriculture"),
        ("B.Tech AI&DS", "B.Tech AI&DS"),
        ("B.Tech CS&IT", "B.Tech CS&IT"),
        ("B.Tech ECS", "B.Tech ECS"),
        ("B.Tech IOT", "B.Tech IOT"),
        ("BBA", "BBA"),
        ("BBA- BA", "BBA- BA"),
        ("BBA-LLB", "BBA-LLB"),
        ("BCA", "BCA"),
        ("B.Tech ECE", "B.Tech ECE"),
        ("B.Tech CSE - Regular", "B.Tech CSE - Regular"),
        ("B.Tech CSE - Honors", "B.Tech CSE - Honors"),
        ("B.Tech BT", "B.Tech BT"),
        ("B.Tech CE", "B.Tech CE"),
        ("B.Tech EEE", "B.Tech EEE"),
        ("B.Tech ME", "B.Tech ME"),
        ("LLB", "LLB"),
        ("M.Pharmacy", "M.Pharmacy"),
        ("M.Sc Computational Mathematics", "M.Sc Computational Mathematics"),
        ("M.Sc Nano Science and Technology", "M.Sc Nano Science and Technology"),
        ("M.Sc Chemistry", "M.Sc Chemistry"),
        ("M.Sc Physics", "M.Sc Physics"),
        ("M.Tech - EVT", "M.Tech - EVT"),
        ("M.Tech - PE & PS", "M.Tech - PE & PS"),
        ("MA DH&LS", "MA DH&LS"),
        ("MA English", "MA English"),
        ("MBA", "MBA"),
        ("MCA", "MCA"),
        ("M.Sc - F&C", "M.Sc - F&C"),
        ("M.Tech - CTM", "M.Tech - CTM"),
        ("M.Tech - Machine Design", "M.Tech - Machine Design"),
        ("M.Tech - SE", "M.Tech - SE"),
        ("M.Tech - Thermal Engineering", "M.Tech - Thermal Engineering"),
        ("M.Tech - CSE", "M.Tech - CSE"),
        ("Pharma D", "Pharma D"),
        ("other", "other"),
        
    ]
    
    Residence_choices = [
        ("", "Select Residence"),
        ("Hostel", "Hostel"),
        ("Day Scholar", "Day Scholar"),
        # ("Outside Hostel", "Outside Hostel"),
    ]
    
    Transport_choices = [
        ("", "Select Transport"),
        ("College Bus", "College Bus"),
        ("Own transport", "Own transport"),
        ("Other", "Other"),
    ]
    
    Bus_Routes_choices = [
        ("", "Select Bus Route"),
        # Guntur Routes
        ("8A", "Bus 8A - Gorantla, Guntur"),
        ("8B", "Bus 8B - Lodge Center, Guntur"),
        ("8C", "Bus 8C - SVN Colony, Guntur"),
        ("8D", "Bus 8D - Golden Gym, Guntur"),
        ("8E", "Bus 8E - Kortipadu, Guntur"),
        ("8F", "Bus 8F - Hanumaiah Company, Guntur"),
        ("8G", "Bus 8G - Seetharamaiah School, Guntur"),
        ("8H", "Bus 8H - Stambala Garuvu, Guntur"),
        ("8I", "Bus 8I - Vengalayapalem, Guntur"),
        ("8J", "Bus 8J - Housing Board, Guntur"),
        ("8K", "Bus 8K - Bus Stand, Guntur"),
        ("8L", "Bus 8L - Bus Stand, Guntur"),
        ("8M", "Bus 8M - Padmaja Petrol Bunk, Guntur"),
        ("8N", "Bus 8N - Hanumaiah Company, Guntur"),
        
        # Tenali Routes
        ("9A", "Bus 9A - Chinaravuri Park, Tenali"),
        ("9B", "Bus 9B - Montissori, Tenali"),
        ("9C", "Bus 9C - Angalakuduru, Tenali"),
        ("9DE", "Bus 9DE - Bus Stand, Tenali"),
        
        # Thulluru Routes
        ("8T", "Bus 8T - Thulluru"),
        
        # Vijayawada Routes
        ("1A", "Bus 1A - Vuyyur, Vijayawada"),
        ("1B", "Bus 1B - Kankipadu, Vijayawada"),
        ("1C", "Bus 1C - Penamalluru, Vijayawada"),
        ("1D", "Bus 1D - Tadigadapa, Vijayawada"),
        ("1E", "Bus 1E - Time Hospital, Vijayawada"),
        ("1F", "Bus 1F - Autonagar Gate, Vijayawada"),
        ("1G", "Bus 1G - Patamata, Vijayawada"),
        ("2A", "Bus 2A - ESI Bus Stop, Vijayawada"),
        ("3AB", "Bus 3AB - ITI Bus Stop, Vijayawada"),
        ("4A", "Bus 4A - Gannavaram, Vijayawada"),
        ("4B", "Bus 4B - Enikepadu, Vijayawada"),
        ("4C", "Bus 4C - Ramavarapadu, Vijayawada"),
        ("4D", "Bus 4D - Bank Colony, Vijayawada"),
        ("5A", "Bus 5A - MG Road, Vijayawada"),
        ("6A", "Bus 6A - Payakapuram, Vijayawada"),
        ("6B", "Bus 6B - Ajit Singh Nagar, Vijayawada"),
        ("6C", "Bus 6C - Raghavendra Theatre, Vijayawada"),
        ("6D1", "Bus 6D1 - Prabhas College, Vijayawada"),
        ("6E", "Bus 6E - Food Junction, Vijayawada"),
        ("6F", "Bus 6F - Madhura Nagar, Vijayawada"),
        ("7A", "Bus 7A - Ibrahimpatnam, Vijayawada"),
        ("7B", "Bus 7B - Ibrahimpatnam, Vijayawada"),
        ("7C", "Bus 7C - Ibrahimpatnam, Vijayawada"),
        ("7D", "Bus 7D - Ibrahimpatnam, Vijayawada"),
        ("7E", "Bus 7E - Ibrahimpatnam, Vijayawada"),
        ("7F", "Bus 7F - Sivalayam, Vijayawada"),
        ("7G", "Bus 7G - Sitara, Vijayawada"),
    ]
    
    # Role_choices = [
    #     # ("","Select Role"),
    #     ("Student","Student"),
    #     ("Super Admin","Super admin"),
    #     ("Club incharge","Club incharge"),
    #     ("Report Manager","Report Manager"),
    # ]
    Role_choices = [
            ('Student', 'Student'),
            ('Club Incharge', 'Club Incharge'),
            ('Report Manager', 'Report Manager'),
            ('Super Admin', 'Super Admin'),
        ]


    # Choices for Year
    Year_choices = [
        (1, "First Year"),
        (2, "Second Year"),
        (3, "Third Year"),
        (4, "Fourth Year"),
    ]
    
    Girls_Hostels=[
        ("", "Select Girls Hostel"),
        ("Kanchana Ganga Hostel", "Kanchana Ganga Hostel"),
        ("Himalaya Girls Hostel", "Himalaya Girls Hostel"),
        ("Outside Hostel", "Outside Hostel"),
    ]
    

    
    
    Gender_choices = [
        ("", "Select Gender"),
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]
    
    Cluster_choices = [
        ("", "Select Cluster"),
        (1, "Cluster 1"),
        (2, "Cluster 2"),
        (3, "Cluster 3"),
    ]

    # Choices for Training
    Training_Choices = [
        ("Personal Training", "Personal Training"),
        ("Club Member", "Club Member"),
    ]
    
    Hostel_boys_Campus_choices = [
        ("", "Select one"),
        ("in campus", "in campus"),
        ("outside campus", "outside campus"),
    ]
    
    hostel_boys_in_campus_choices = [
        ("", "Select Hostel"),
        ("Tulip Residency", "Tulip Residency"),
        ("Aravali & Vindhya", "Aravali & Vindhya"),
        ("Kailash Residency", "Kailash Residency"),
    ]
    hostel_boys_outside_campus_choices = [
        ("", "Select Hostel"),
        ("Tirumala", "Tirumala"),
        ("Sahyadri", "Sahyadri"),
        ("Satpura", "Satpura"),
        ("Nilagiri", "Nilagiri"),
        ("Archies", "Archies"),
        ("Malabar", "Malabar"),
    ]
    
    country_choices = [
        ("", "Select Country"),
        ("Afghanistan", "Afghanistan"),
        ("Albania", "Albania"),
        ("Algeria", "Algeria"),
        ("Andorra", "Andorra"),
        ("Angola", "Angola"),
        ("Antigua and Barbuda", "Antigua and Barbuda"),
        ("Argentina", "Argentina"),
        ("Armenia", "Armenia"),
        ("Australia", "Australia"),
        ("Austria", "Austria"),
        ("Azerbaijan", "Azerbaijan"),
        ("Bahamas", "Bahamas"),
        ("Bahrain", "Bahrain"),
        ("Bangladesh", "Bangladesh"),
        ("Barbados", "Barbados"),
        ("Belarus", "Belarus"),
        ("Belgium", "Belgium"),
        ("Belize", "Belize"),
        ("Benin", "Benin"),
        ("Bhutan", "Bhutan"),
        ("Bolivia", "Bolivia"),
        ("Bosnia and Herzegovina", "Bosnia and Herzegovina"),
        ("Botswana", "Botswana"),
        ("Brazil", "Brazil"),
        ("Brunei", "Brunei"),
        ("Bulgaria", "Bulgaria"),
        ("Burkina Faso", "Burkina Faso"),
        ("Burundi", "Burundi"),
        ("Cabo Verde", "Cabo Verde"),
        ("Cambodia", "Cambodia"),
        ("Cameroon", "Cameroon"),
        ("Central African Republic", "Central African Republic"),
        ("Chad", "Chad"),
        ("Chile", "Chile"),
        ("China", "China"),
        ("Colombia", "Colombia"),
        ("Comoros", "Comoros"),
        ("Congo (Congo-Brazzaville)", "Congo (Congo-Brazzaville)"),
        ("Congo (DRC)", "Congo (DRC)"),
        ("Costa Rica", "Costa Rica"),
        ("Côte d'Ivoire", "Côte d'Ivoire"),
        ("Croatia", "Croatia"),
        ("Cuba", "Cuba"),
        ("Cyprus", "Cyprus"),
        ("Czechia (Czech Republic)", "Czechia (Czech Republic)"),
        ("Denmark", "Denmark"),
        ("Djibouti", "Djibouti"),
        ("Dominica", "Dominica"),
        ("Dominican Republic", "Dominican Republic"),
        ("Ecuador", "Ecuador"),
        ("Egypt", "Egypt"),
        ("El Salvador", "El Salvador"),
        ("Equatorial Guinea", "Equatorial Guinea"),
        ("Eritrea", "Eritrea"),
        ("Estonia", "Estonia"),
        ("Ethiopia", "Ethiopia"),
        ("Fiji", "Fiji"),
        ("Finland", "Finland"),
        ("France", "France"),
        ("Gabon", "Gabon"),
        ("Gambia", "Gambia"),
        ("Georgia", "Georgia"),
        ("Germany", "Germany"),
        ("Ghana", "Ghana"),
        ("Greece", "Greece"),
        ("Grenada", "Grenada"),
        ("Guatemala", "Guatemala"),
        ("Guinea", "Guinea"),
        ("Guyana", "Guyana"),
        ("Haiti", "Haiti"),
        ("Holy See", "Holy See"),
        ("Honduras", "Honduras"),
        ("Hungary", "Hungary"),
        ("Iceland", "Iceland"),
        ("India", "India"),
        ("Indonesia", "Indonesia"),
        ("Iran", "Iran"),
        ("Iraq", "Iraq"),
        ("Ireland", "Ireland"),
        ("Israel", "Israel"),
        ("Italy", "Italy"),
        ("Jamaica", "Jamaica"),
        ("Japan", "Japan"),
        ("Jordan", "Jordan"),
        ("Kazakhstan", "Kazakhstan"),
        ("Kenya", "Kenya"),
        ("Kiribati", "Kiribati"),   
        ("Kuwait", "Kuwait"),
        ("Kyrgyzstan", "Kyrgyzstan"),
        ("Laos", "Laos"),
        ("Latvia", "Latvia"),
        ("Lebanon", "Lebanon"),
        ("Lesotho", "Lesotho"),
        ("Liberia", "Liberia"),
        ("Libya", "Libya"), 
        ("Liechtenstein", "Liechtenstein"),
        ("Lithuania", "Lithuania"),
        ("Luxembourg", "Luxembourg"),
        ("Madagascar", "Madagascar"),
        ("Malawi", "Malawi"),
        ("Malaysia", "Malaysia"),
        ("Maldives", "Maldives"),
        ("Mali", "Mali"),
        ("Malta", "Malta"),
        ("Marshall Islands", "Marshall Islands"),
        ("Mauritania", "Mauritania"),
        ("Mauritius", "Mauritius"),
        ("Mexico", "Mexico"),
        ("Micronesia", "Micronesia"),
        ("Moldova", "Moldova"),
        ("Monaco", "Monaco"),
        ("Mongolia", "Mongolia"),
        ("Montenegro", "Montenegro"),
        ("Morocco", "Morocco"),
        ("Mozambique", "Mozambique"),
        ("Myanmar", "Myanmar"),
        ("Namibia", "Namibia"),
        ("Nauru", "Nauru"),
        ("Nepal", "Nepal"),
        ("Netherlands", "Netherlands"),
        ("New Zealand", "New Zealand"),
        ("Nicaragua", "Nicaragua"),
        ("Niger", "Niger"),
        ("Nigeria", "Nigeria"),
        ("North Macedonia", "North Macedonia"),
        ("Norway", "Norway"),
        ("Oman", "Oman"),
        ("Pakistan", "Pakistan"),
        ("Palau", "Palau"),
        ("Palestine State", "Palestine State"),
        ("Panama", "Panama"),
        ("Papua New Guinea", "Papua New Guinea"),
        ("Paraguay", "Paraguay"),
        ("Peru", "Peru"),
        ("Philippines", "Philippines"),
        ("Poland", "Poland"),
        ("Portugal", "Portugal"),
        ("Qatar", "Qatar"), 
        ("Romania", "Romania"),
        ("Russia", "Russia"),
        ("Rwanda", "Rwanda"),
        ("Saint Kitts and Nevis", "Saint Kitts and Nevis"),
        ("Saint Lucia", "Saint Lucia"),
        ("Saint Vincent and the Grenadines", "Saint Vincent and the Grenadines"),
        ("Samoa", "Samoa"),
        ("San Marino", "San Marino"),
        ("Sao Tome and Principe", "Sao Tome and Principe"), 
        ("Saudi Arabia", "Saudi Arabia"),
        ("Senegal", "Senegal"),
        ("Serbia", "Serbia"),
        ("Seychelles", "Seychelles"),
        ("Sierra Leone", "Sierra Leone"),
        ("Singapore", "Singapore"),
        ("Slovakia", "Slovakia"),
        ("Slovenia", "Slovenia"),
        ("Solomon Islands", "Solomon Islands"), 
        ("Somalia", "Somalia"),
        ("South Africa", "South Africa"),
        ("South Korea", "South Korea"),
        ("South Sudan", "South Sudan"),
        ("Spain", "Spain"),
        ("Sri Lanka", "Sri Lanka"), 
        ("Sudan", "Sudan"),
        ("Suriname", "Suriname"),
        ("Sweden", "Sweden"),
        ("Switzerland", "Switzerland"),
        ("Syria", "Syria"),
        ("Tajikistan", "Tajikistan"),
        ("Tanzania", "Tanzania"),
        ("Thailand", "Thailand"),
        ("Timor-Leste", "Timor-Leste"),
        ("Togo", "Togo"),
        ("Tonga", "Tonga"),
        ("Trinidad and Tobago", "Trinidad and Tobago"),
        ("Tunisia", "Tunisia"),
        ("Turkey", "Turkey"),
        ("Turkmenistan", "Turkmenistan"),
        ("Tuvalu", "Tuvalu"),
        ("Uganda", "Uganda"),
        ("Ukraine", "Ukraine"),
        ("United Arab Emirates", "United Arab Emirates"),
        ("United Kingdom", "United Kingdom"),
        ("United States of America", "United States of America"),
        ("Uruguay", "Uruguay"),
        ("Uzbekistan", "Uzbekistan"),
        ("Vanuatu", "Vanuatu"),
        ("Venezuela", "Venezuela"),
        ("Vietnam", "Vietnam"),
        ("Yemen", "Yemen"),
        ("Zambia", "Zambia"),
        ("Zimbabwe", "Zimbabwe"),
        ("other", "other"),
    ]
    
    State_choices = [
        ("", "Select State"),
        ("Andhra Pradesh", "Andhra Pradesh"),
        ("Arunachal Pradesh", "Arunachal Pradesh"),
        ("Assam", "Assam"),
        ("Bihar", "Bihar"),
        ("Chhattisgarh", "Chhattisgarh"),
        ("Goa", "Goa"),
        ("Gujarat", "Gujarat"),
        ("Haryana", "Haryana"),
        ("Himachal Pradesh", "Himachal Pradesh"),
        ("Jharkhand", "Jharkhand"),
        ("Karnataka", "Karnataka"),
        ("Kerala", "Kerala"),
        ("Madhya Pradesh", "Madhya Pradesh"),
        ("Maharashtra", "Maharashtra"),
        ("Manipur", "Manipur"),
        ("Meghalaya", "Meghalaya"),
        ("Mizoram", "Mizoram"),
        ("Nagaland", "Nagaland"),
        ("Odisha", "Odisha"),
        ("Punjab", "Punjab"),
        ("Rajasthan", "Rajasthan"),
        ("Sikkim", "Sikkim"),
        ("Tamil Nadu", "Tamil Nadu"),
        ("Telangana", "Telangana"),
        ("Tripura", "Tripura"),
        ("Uttar Pradesh", "Uttar Pradesh"),
        ("Uttarakhand", "Uttarakhand"),
        ("West Bengal", "West Bengal"),
        ("other", "other"),
    ]
    
    

    # Step 1: Initial Registration Fields (Required)
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=128, null=True, blank=True)  # Allow null temporarily
    role = models.CharField(max_length=20, choices=Role_choices, default="Student")
    
    # Step 2: Basic Information (Required to proceed)
    name = models.CharField(max_length=50, null=True, blank=True)
    mobile_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    
    # Step 3: Academic Information
    branch = models.CharField(max_length=32, choices=Branch_choices, null=True, blank=True)
    year = models.IntegerField(choices=Year_choices, null=True, blank=True)
    training_type = models.CharField(max_length=20, choices=Training_Choices, null=True, blank=True)
    
    # Step 4: Personal Information
    gender = models.CharField(max_length=10, choices=Gender_choices, null=True, blank=True)
    residence = models.CharField(max_length=15, choices=Residence_choices, null=True, blank=True)
    girls_hostel = models.CharField(max_length=21, choices=Girls_Hostels, null=True, blank=True)
    hostel_boys_campus = models.CharField(max_length=15, choices=Hostel_boys_Campus_choices, null=True, blank=True)
    hostel_boys_in_campus = models.CharField(max_length=17, choices=hostel_boys_in_campus_choices, null=True, blank=True)
    hostel_boys_outside_campus = models.CharField(max_length=15, choices=hostel_boys_outside_campus_choices, null=True, blank=True)
    transport = models.CharField(max_length=15, choices=Transport_choices, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bus_route = models.CharField(max_length=15, choices=Bus_Routes_choices, null=True, blank=True)
    
    # Step 5: Location Information
    cluster = models.IntegerField(choices=Cluster_choices, null=True, blank=True)
    country = models.CharField(max_length=100, choices=country_choices, null=True, blank=True)
    state = models.CharField(max_length=100, choices=State_choices, null=True, blank=True)

    # Profile completion tracker
    is_profile_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"({self.username} {self.branch} {self.year})"

    def is_step2_complete(self):
        return all([self.name, self.mobile_number, self.email])

    def is_step3_complete(self):
        return all([self.branch, self.year, self.training_type])

    def is_step4_complete(self):
        return all([self.residence, self.date_of_birth, self.gender])

    def is_step5_complete(self):
        return all([self.cluster, self.country, self.state])

    def save(self, *args, **kwargs):
        # Set password as date of birth when it's provided
        if self.date_of_birth and not self.password:
            self.password = self.date_of_birth.strftime('%Y%m%d')  # Format: YYYYMMDD
            
        # Check profile completion
        if all([
            self.is_step2_complete(),
            self.is_step3_complete(),
            self.is_step4_complete(),
            self.is_step5_complete()
        ]):
            self.is_profile_complete = True
        else:
            self.is_profile_complete = False
            
        super().save(*args, **kwargs)
    
    
    

