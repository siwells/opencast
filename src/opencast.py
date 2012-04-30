import urllib2

def pretty_print_file():
    file_name = "design.json"
    with open(file_name, 'r') as file:
    infile = json.load(file)
    outfile = "pp_"+file_name
    with open(outfile, 'w') as file:
        file.write(json.dumps(infile, sort_keys=False, indent=4))

def retrieve_issues():
    file_name = "design.json"
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(realm='Redmine API', uri='https://developers.superhub-project.eu/projects/wp1/issues.json', user='swells', passwd='marma1ad3')

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