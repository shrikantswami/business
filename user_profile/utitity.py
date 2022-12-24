
class Utility:

    @staticmethod
    def extract_user_detais(request):
        try:
            data = {}
            data['username'] = request.data.get('email', request.data['username'])['value'].split('@')[0]
            data['email'] = request.data.get('email',{}).get('value')
            data['password'] = request.data['password']['value']
            data['first_name'] = request.data.get('firstName',{}).get('value')
            data['middle_name'] = request.data.get('middleName',{}).get('value')
            data['last_name'] = request.data.get('lastName',{}).get('value')
            return data
        except Exception as e:
            print(str(e))
            return {}