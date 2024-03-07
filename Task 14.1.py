#Q1. Using the given URL, write a python program #

import requests

class Users:
    def __init__(self, url):  
         # Initialize the class with the provided URL      
        self.url = url
        self.response = requests.get(url)
   
    def isConnected(self):
         # To Check if the connection to the URL is successful (HTTP status code 200)
        if self.response.status_code == 200:
            return True
        return False

    def fetchData(self):
        try:
             # To Check if the connection is successful and return the JSON data
            if self.isConnected():
                return self.response.json()
            raise Exception()
        except:
            print("It is not connected")
            return None
       
    def getCountryNames(self):
        countryNamesList = []

        data = self.fetchData()
        if data and isinstance(data, list):
             # Iterate through the list and extract common names of countries
            for countryDict in data:
                if 'name' in countryDict:
                    countryNamesList.append(countryDict["name"]["common"])
            return countryNamesList
        else:
            print("It is not connected to country data")

    def getCurrencyNames(self):
        currencyNamesList = []

        data = self.fetchData()
        if data and isinstance(data, list):
             # Iterate through the list and extract currency names
            for countryDict in data:
                if 'currencies' in countryDict:
                    for currency_code, currencyDict in countryDict["currencies"].items():
                        if 'name' in currencyDict:
                            currencyNamesList.append(currencyDict["name"])
            return currencyNamesList
        else:
            print("It is not connected to currency data")

    def getCurrencySymbols(self):
        currencySymbolsList = []

        data = self.fetchData()
        if data and isinstance(data, list):
            # Iterate through the list and extract currency symbols
            for countryDict in data:
                if 'currencies' in countryDict:
                    for currency_code, currencyDict in countryDict["currencies"].items():
                        if 'symbol' in currencyDict:
                            currencySymbolsList.append(currencyDict["symbol"])
            return currencySymbolsList
        else:
            print("It is not connected to currency data")

    def getCountriesDollarCurrency(self):
        dollarCountriesList = []

        data = self.fetchData()
        if data and isinstance(data, list):
             # Iterate through the list and extract countries with Dollar currency
            for countryDict in data:
                if 'currencies' in countryDict:
                    for currency_code, currencyDict in countryDict["currencies"].items():
                        if currencyDict.get("symbol") == "$":
                            dollarCountriesList.append(countryDict["name"]["common"])
            return dollarCountriesList
        else:
            print("It is not connected to currency data")

    def getCountriesEuroCurrency(self):
        euroCountriesList = []

        data = self.fetchData()
        if data and isinstance(data, list):
             # Iterate through the list and extract countries with Euro currency
            for countryDict in data:
                if 'currencies' in countryDict:
                    for currency_code, currencyDict in countryDict["currencies"].items():
                        if currencyDict.get("symbol") == "€":
                            euroCountriesList.append(countryDict["name"]["common"])
            return euroCountriesList
        else:
            print("It is not connected to currency data")

    


url = "https://restcountries.com/v3.1/all"
userObj = Users(url)
print(userObj.getCountryNames())
print(userObj.getCurrencyNames())
print(userObj.getCurrencySymbols())
print(userObj.getCountriesDollarCurrency())
print(userObj.getCountriesEuroCurrency())

#Output- ['Cyprus', 'Eritrea', 'Liberia', 'Bermuda', 'Vatican City', 'Cook Islands', 'Somalia', 'Zambia', 'Venezuela', 'Turkmenistan', 'Albania', 'Croatia', 'United Kingdom', 'Sudan', 'Timor-Leste', 'Republic of the Congo', 'Azerbaijan', 'Kenya', 'American Samoa', 'Ivory Coast', 'Senegal', 'Vietnam', 'El Salvador', 'Afghanistan', 'Saint Martin', 'Latvia', 'Guatemala', 'Kuwait', 'São Tomé and Príncipe', 'Kyrgyzstan', 'Poland', 'Guam', 'Ghana', 'Lithuania', 'Armenia', 'Jersey', 'Grenada', 'Tajikistan', 'Ethiopia', 'Western Sahara', 'Morocco', 'Puerto Rico', 'Christmas Island', 'New Zealand', 'Brunei', 'French Guiana', 'Niue', 'Romania', 'Svalbard and Jan Mayen', 'Belarus', 'Panama', 'Cameroon', 'Czechia', 'Saint Barthélemy', 'Greece', 'Mali', 'Martinique', 'France', 'Pakistan', 'Peru', 'Barbados', 'Greenland', 'Saint Pierre and Miquelon', 'Chad', 'Hungary', 'Comoros', 'Bangladesh', 'Tokelau', 'Fiji', 'China', 'Colombia', 'British Virgin Islands', 'Algeria', 'Maldives', 'Malaysia', 'Cayman Islands', 'Spain', 'Ireland', 'Estonia', 'Paraguay', 'Uruguay', 'South Africa', 'Saint Lucia', 'Vanuatu', 'Finland', 'Sweden', 'British Indian Ocean Territory', 'Lebanon', 'United States', 'Chile', 'Norfolk Island', 'Montserrat', 'Australia', 'Belize', 'Guyana', 'Mongolia', 'Tuvalu', 'Dominican Republic', 'Equatorial Guinea', 'Saint Kitts and Nevis', 'Bolivia', 'Nepal', 'French Southern and Antarctic Lands', 'Taiwan', 'Benin', 'Bulgaria', 'Moldova', 'Isle of Man', 'Bhutan', 'Cambodia', 'Antigua and Barbuda', 'Haiti', 'Cape Verde', 'Georgia', 'Burundi', 'Bahamas', 'Mauritius', 'Libya', 'Malawi', 'Mexico', 'Eswatini', 'Papua New Guinea', 'Dominica', 'Liechtenstein', 'Russia', 'Israel', 'Singapore', 'Uganda', 'Slovakia', 'Tonga', 'United Arab Emirates', 'Mayotte', 'Suriname', 'Uzbekistan', 'Saudi Arabia', 'Egypt', 'Italy', 'Madagascar', 'New Caledonia', 'Canada', 'United States Virgin Islands', 'Marshall Islands', 'Mauritania', 'Gambia', 'Trinidad and Tobago', 'Seychelles', 'Japan', 'Brazil', 'Syria', 'Saint Helena, Ascension and Tristan da Cunha', 'Tanzania', 'Andorra', 'Iran', 'Togo', 'Malta', 'South Korea', 'Samoa', 'Germany', 'Niger', 'Bouvet Island', 'Jamaica', 'Nicaragua', 'Guinea', 'Anguilla', 'Åland Islands', 'Belgium', 'Portugal', 'Denmark', 'Philippines', 'Wallis and Futuna', 'Austria', 'Guinea-Bissau', 'Monaco', 'Namibia', 'United States Minor Outlying Islands', 'Costa Rica', 'Bosnia and Herzegovina', 'Macau', 'Mozambique', 'Réunion', 'Montenegro', 'North Korea', 'Northern Mariana Islands', 'Ukraine', 'Iraq', 'South Georgia', 'Angola', 'Sierra Leone', 'Micronesia', 'Cuba', 'Turks and Caicos Islands', 'Serbia', 'Ecuador', 'Faroe Islands', 'Antarctica', 'Palestine', 'Turkey', 'Kiribati', 'Kazakhstan', 'Gibraltar', 'Iceland', 'Palau', 'Qatar', 'Switzerland', 'French Polynesia', 'Pitcairn Islands', 'Jordan', 'Myanmar', 'Thailand', 'Caribbean Netherlands', 'Aruba', 'Guadeloupe', 'Nigeria', 'Bahrain', 'Laos', 'Cocos (Keeling) Islands', 'Djibouti', 'Solomon Islands', 'Heard Island and McDonald Islands', 'India', 'San Marino', 'Luxembourg', 'Sint Maarten', 'Falkland Islands', 'Central African Republic', 'Botswana', 'Curaçao', 'Guernsey', 'Norway', 'Gabon', 'Zimbabwe', 'Lesotho', 'Slovenia', 'Argentina', 'Burkina Faso', 'Yemen', 'DR Congo', 'Oman', 'Indonesia', 'Nauru', 'Rwanda', 'North Macedonia', 'Kosovo', 'Netherlands', 'Tunisia', 'South Sudan', 'Honduras', 'Saint Vincent and the Grenadines', 'Sri Lanka', 'Hong Kong'];       ['Euro', 'Eritrean nakfa', 'Liberian dollar', 'Bermudian dollar', 'Euro', 'Cook Islands dollar', 'New Zealand dollar', 'Somali shilling', 'Zambian kwacha', 'Venezuelan bolívar soberano', 'Turkmenistan manat', 'Albanian lek', 'Euro', 'British pound', 'Sudanese pound', 'United States dollar', 'Central African CFA franc', 'Azerbaijani manat', 'Kenyan shilling', 'United States dollar', 'West African CFA franc', 'West African CFA franc', 'Vietnamese đồng', 'United States dollar', 'Afghan afghani', 'Euro', 'Euro', 'Guatemalan quetzal', 'Kuwaiti dinar', 'São Tomé and Príncipe dobra', 'Kyrgyzstani som', 'Polish złoty', 'United States dollar', 'Ghanaian cedi', 'Euro', 'Armenian dram', 'British pound', 'Jersey pound', 'Eastern Caribbean dollar', 'Tajikistani somoni', 'Ethiopian birr', 'Algerian dinar', 'Moroccan dirham', 'Mauritanian ouguiya', 'Moroccan dirham', 'United States dollar', 'Australian dollar', 'New Zealand dollar', 'Brunei dollar', 'Singapore dollar', 'Euro', 'New Zealand dollar', 'Romanian leu', 'krone', 'Belarusian ruble', 'Panamanian balboa', 'United States dollar', 'Central African CFA franc', 'Czech koruna', 'Euro', 'Euro', 'West African CFA franc', 'Euro', 'Euro', 'Pakistani rupee', 'Peruvian sol', 'Barbadian dollar', 'krone', 'Euro', 'Central African CFA franc', 'Hungarian forint', 'Comorian franc', 'Bangladeshi taka', 'New Zealand dollar', 'Fijian dollar', 'Chinese yuan', 'Colombian peso', 'United States dollar', 'Algerian dinar', 'Maldivian rufiyaa', 'Malaysian ringgit', 'Cayman Islands dollar', 'Euro', 'Euro', 'Euro', 'Paraguayan guaraní', 'Uruguayan peso', 'South African rand', 'Eastern Caribbean dollar', 'Vanuatu vatu', 'Euro', 'Swedish krona', 'United States dollar', 'Lebanese pound', 'United States dollar', 'Chilean peso', 'Australian dollar', 'Eastern Caribbean dollar', 'Australian dollar', 'Belize dollar', 'Guyanese dollar', 'Mongolian tögrög', 'Australian dollar', 'Tuvaluan dollar', 'Dominican peso', 'Central African CFA franc', 'Eastern Caribbean dollar', 'Bolivian boliviano', 'Nepalese rupee', 'Euro', 'New Taiwan dollar', 'West African CFA franc', 'Bulgarian lev', 'Moldovan leu', 'British pound', 'Manx pound', 'Bhutanese ngultrum', 'Indian rupee', 'Cambodian riel', 'United States dollar', 'Eastern Caribbean dollar', 'Haitian gourde', 'Cape Verdean escudo', 'lari', 'Burundian franc', 'Bahamian dollar', 'United States dollar', 'Mauritian rupee', 'Libyan dinar', 'Malawian kwacha', 'Mexican peso', 'Swazi lilangeni', 'South African rand', 'Papua New Guinean kina', 'Eastern Caribbean dollar', 'Swiss franc', 'Russian ruble', 'Israeli new shekel', 'Singapore dollar', 'Ugandan shilling', 'Euro', 'Tongan paʻanga', 'United Arab Emirates dirham', 'Euro', 'Surinamese dollar', 'Uzbekistani soʻm', 'Saudi riyal', 'Egyptian pound', 'Euro', 'Malagasy ariary', 'CFP franc', 'Canadian dollar', 'United States dollar', 'United States dollar', 'Mauritanian ouguiya', 'dalasi', 'Trinidad and Tobago dollar', 'Seychellois rupee', 'Japanese yen', 'Brazilian real', 'Syrian pound', 'Pound sterling', 'Saint Helena pound', 'Tanzanian shilling', 'Euro', 'Iranian rial', 'West African CFA franc', 'Euro', 'South Korean won', 'Samoan tālā', 'Euro', 'West African CFA franc', 'Jamaican dollar', 'Nicaraguan córdoba', 'Guinean franc', 'Eastern Caribbean dollar', 'Euro', 'Euro', 'Euro', 'Danish krone', 'Philippine peso', 'CFP franc', 'Euro', 'West African CFA franc', 'Euro', 'Namibian dollar', 'South African rand', 'United States dollar', 'Costa Rican colón', 'Bosnia and Herzegovina convertible mark', 'Macanese pataca', 'Mozambican metical', 'Euro', 'Euro', 'North Korean won', 'United States dollar', 'Ukrainian hryvnia', 'Iraqi dinar', 'Saint Helena pound', 'Angolan kwanza', 'Sierra Leonean leone', 'United States dollar', 'Cuban convertible peso', 'Cuban peso', 'United States dollar', 'Serbian dinar', 'United States dollar', 'Danish krone', 'Faroese króna', 'Egyptian pound', 'Israeli new shekel', 'Jordanian dinar', 'Turkish lira', 'Australian dollar', 'Kiribati dollar', 'Kazakhstani tenge', 'Gibraltar pound', 'Icelandic króna', 'United States dollar', 'Qatari riyal', 'Swiss franc', 'CFP franc', 'New Zealand dollar', 'Jordanian dinar', 'Burmese kyat', 'Thai baht', 'United States dollar', 'Aruban florin', 'Euro', 'Nigerian naira', 'Bahraini dinar', 'Lao kip', 'Australian dollar', 'Djiboutian franc', 'Solomon Islands dollar', 'Indian rupee', 'Euro', 'Euro', 'Netherlands Antillean guilder', 'Falkland Islands pound', 'Central African CFA franc', 'Botswana pula', 'Netherlands Antillean guilder', 'British pound', 'Guernsey pound', 'Norwegian krone', 'Central African CFA franc', 'Zimbabwean dollar', 'Lesotho loti', 'South African rand', 'Euro', 'Argentine peso', 'West African CFA franc', 'Yemeni rial', 'Congolese franc', 'Omani rial', 'Indonesian rupiah', 'Australian dollar', 'Rwandan franc', 'denar', 'Euro', 'Euro', 'Tunisian dinar', 'South Sudanese pound', 'Honduran lempira', 'Eastern Caribbean dollar', 'Sri Lankan rupee', 'Hong Kong dollar'];           ['€', 'Nfk', '$', '$', '€', '$', '$', 'Sh', 'ZK', 'Bs.S.', 'm', 'L', '€', '£', '$', 'Fr', '₼', 'Sh', '$', 'Fr', 'Fr', '₫', '$', '؋', '€', '€', 'Q', 'د.ك', 'Db', 'с', 'zł', '$', '₵', '€', '֏', '£', '£', '$', 'ЅМ', 'Br', 'دج', 'DH', 'UM', 'د.م.', '$', '$', '$', '$', '$', '€', '$', 'lei', 'kr', 'Br', 'B/.', '$', 'Fr', 'Kč', '€', '€', 'Fr', '€', '€', '₨', 'S/ ', '$', 'kr.', '€', 'Fr', 'Ft', 'Fr', '৳', '$', '$', '¥', '$', '$', 'د.ج', '.ރ', 'RM', '$', '€', '€', '€', '₲', '$', 'R', '$', 'Vt', '€', 'kr', '$', 'ل.ل', '$', '$', '$', '$', '$', '$', '$', '₮', '$', '$', '$', 'Fr', '$', 'Bs.', '₨', '€', '$', 'Fr', 'лв', 'L', '£', '£', 'Nu.', '₹', '៛', '$', '$', 'G', 'Esc', '₾', 'Fr', '$', '$', '₨', 'ل.د', 'MK', '$', 'L', 'R', 'K', '$', 'Fr', '₽', '₪', '$', 'Sh', '€', 'T$', 'د.إ', '€', '$', "so'm", 'ر.س', '£', '€', 'Ar', '₣', '$', '$', '$', 'UM', 'D', '$', '₨', '¥', 'R$', '£', '£', '£', 'Sh', '€', '﷼', 'Fr', '€', '₩', 'T', '€', 'Fr', '$', 'C$', 'Fr', '$', '€', '€', '€', 'kr', '₱', '₣', '€', 'Fr', '€', '$', 'R', '$', '₡', 'P', 'MT', '€', '€', '₩', '$', '₴', 'ع.د', '£', 'Kz', 'Le', '$', '$', '$', '$', 'дин.', '$', 'kr', 'kr', 'E£', '₪', 'JD', '₺', '$', '$', '₸', '£', 'kr', '$', 'ر.ق', 'Fr.', '₣', '$', 'د.ا', 'Ks', '฿', '$', 'ƒ', '€', '₦', '.د.ب', '₭', '$', 'Fr', '$', '₹', '€', '€', 'ƒ', '£', 'Fr', 'P', 'ƒ', '£', '£', 'kr', 'Fr', '$', 'L', 'R', '€', '$', 'Fr', '﷼', 'FC', 'ر.ع.', 'Rp', '$', 'Fr', 'den', '€', '€', 'د.ت', '£', 'L', '$', 'Rs  රු', '$'];       ['Liberia', 'Bermuda', 'Cook Islands', 'Cook Islands', 'Timor-Leste', 'American Samoa', 'El Salvador', 'Guam', 'Grenada', 'Puerto Rico', 'Christmas Island', 'New Zealand', 'Brunei', 'Brunei', 'Niue', 'Panama', 'Barbados', 'Tokelau', 'Fiji', 'Colombia', 'British Virgin Islands', 'Cayman Islands', 'Uruguay', 'Saint Lucia', 'British Indian Ocean Territory', 'United States', 'Chile', 'Norfolk Island', 'Montserrat', 'Australia', 'Belize', 'Guyana', 'Tuvalu', 'Tuvalu', 'Dominican Republic', 'Saint Kitts and Nevis', 'Taiwan', 'Cambodia', 'Antigua and Barbuda', 'Bahamas', 'Bahamas', 'Mexico', 'Dominica', 'Singapore', 'Suriname', 'Canada', 'United States Virgin Islands', 'Marshall Islands', 'Trinidad and Tobago', 'Jamaica', 'Anguilla', 'Namibia', 'United States Minor Outlying Islands', 'Northern Mariana Islands', 'Micronesia', 'Cuba', 'Cuba', 'Turks and Caicos Islands', 'Ecuador', 'Kiribati', 'Kiribati', 'Palau', 'Pitcairn Islands', 'Caribbean Netherlands', 'Cocos (Keeling) Islands', 'Solomon Islands', 'Zimbabwe', 'Argentina', 'Nauru', 'Saint Vincent and the Grenadines', 'Hong Kong'];      ['Cyprus', 'Vatican City', 'Croatia', 'Saint Martin', 'Latvia', 'Lithuania', 'French Guiana', 'Saint Barthélemy', 'Greece', 'Martinique', 'France', 'Saint Pierre and Miquelon', 'Spain', 'Ireland', 'Estonia', 'Finland', 'French Southern and Antarctic Lands', 'Slovakia', 'Mayotte', 'Italy', 'Andorra', 'Malta', 'Germany', 'Åland Islands', 'Belgium', 'Portugal', 'Austria', 'Monaco', 'Réunion', 'Montenegro', 'Guadeloupe', 'San Marino', 'Luxembourg', 'Slovenia', 'Kosovo', 'Netherlands']