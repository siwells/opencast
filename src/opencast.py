import json
import urllib2

issues_file = "design.json"

def description(issue_id):
    with open(issues_file, 'r') as file:
        issues = json.load(file)
    for i in range(len(issues["issues"])):
        if issue_id == issues["issues"][i]["id"]:
            return issues["issues"][i]["description"]
    return None

def num_issues():
    with open(issues_file, 'r') as file:
        issues = json.load(file)
    return len(issues["issues"])
    
def subjects():
    with open(issues_file, 'r') as file:
        issues = json.load(file)
    subjects = []
    for i in range(len(issues["issues"])):
        subjects.append(issues["issues"][i]["subject"])
    return subjects

def pretty_print_file():
    file_name = "design.json"
    with open(file_name, 'r') as file:
        infile = json.load(file)
    outfile = "pp_"+file_name
    with open(outfile, 'w') as file:
        file.write(json.dumps(infile, sort_keys=False, indent=4))

def pretty_print_screen(file_name):
    with open(file_name, 'r') as file:
        infile = json.load(file)
    print json.dumps(infile, sort_keys = False, indent = 4)

def retrieve_issues(user, passwd):
    file_name = "design.json"
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(realm='Redmine API', uri='https://developers.superhub-project.eu/projects/wp1/issues.json', user=user, passwd=passwd)

    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    try: 
        result = urllib2.urlopen("https://developers.superhub-project.eu/projects/wp1/issues.json?tracker_id=14")#&limit=1")
        with open(file_name, 'w') as file:
            for line in result:
                file.write(line)            

    except urllib2.HTTPError, e:
        print e.headers
        #print e.headers['www-authenticate']
        #print e


if __name__ == '__main__':
    print "OpenCast :: The RedMine Requirements Document Generator"