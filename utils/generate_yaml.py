import yaml


def generate_yaml(dep_name, acrname, version, docker_image):
    with open('utils/dep-name.yaml', "r") as stream:
        docs = yaml.load_all(stream)
        dict_docs = []
        for doc in docs:
            dict_docs.append(doc)

    dict_docs[0]['metadata']['name'] = dep_name
    dict_docs[0]['spec']['selector']['matchLabels']['app'] = dep_name
    dict_docs[0]['spec']['template']['metadata']['labels']['app'] = dep_name
    dict_docs[0]['spec']['selector']['matchLabels']['app'] = dep_name
    dict_docs[0]['spec']['template']['spec']['containers'][0]['name'] = dep_name
    dict_docs[0]['spec']['template']['spec']['containers'][0]['image'] = acrname + \
        '.azurecr.io/'+docker_image+':' + version
    dict_docs[1]['metadata']['name'] = dep_name
    dict_docs[1]['spec']['selector']['app'] = dep_name

    with open('utils/'+dep_name+'.yaml', 'a') as outfile:
        yaml.dump(dict_docs[0], outfile, default_flow_style=False)
        outfile.write('--- \n')
        yaml.dump(dict_docs[1], outfile, default_flow_style=False)
