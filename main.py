import streamlit as st
from PIL import Image
import subprocess
from utils.generate_yaml import *
import pandas as pd

# import time
# with st.empty():
#     for seconds in range(60):
#         st.write(f"⏳ {seconds} seconds have passed")
#         time.sleep(1)
#     st.write("✔️ 1 minute over!")
fav = Image.open('images/fav.png')
st.beta_set_page_config(
    page_title='kudle', page_icon=fav, initial_sidebar_state='auto')
# st.title('kudle v0.1')
image = Image.open('images/logo1.png')
st.image(image, width=200)


def run_command_login(args):
    # st.info(f"Running '{' '.join(args)}'")
    output = subprocess.getoutput(args)
    # st.info(output)
    with placeholder3.beta_container():
        st.text(str(output))


def run_command_getip(args):
    # st.info(f"Running '{' '.join(args)}'")
    output = subprocess.getoutput(args)
    # st.info(output)
    try:
        output_mod = output.split(' ')
        # index_ = output_mod.index('AGE\napi-app')
        # df = pd.DataFrame(columns=['App Name', 'Public IP'])
        # df.loc[0] = [output_mod[36].split('\n')[1]] + [output_mod[48]]
        with placeholder4.beta_container():
            # st.write(output_mod[46])
            st.text(output)
            # st.table(df)
    except:
        with placeholder4.beta_container():
            st.write('Sorry, no data')


def run_command(args):
    # st.info(f"Running '{' '.join(args)}'")
    output = subprocess.getoutput(args)
    # st.info(output)
    with placeholder2.beta_container():
        st.text(str(output))


if st.button('Login to your azure account'):
    placeholder3 = st.empty()
    run_command_login('az login')


# check for running nodes
# run_command('az login')

with st.beta_expander("New Deployment"):
    st.markdown('## New Kubernetes Deployment')

    # repo_link = st.text_input('GitHub repo link of your project', '')
    docker_image = st.text_input('Your docker image name', '')
    dep_name = st.text_input('Deployment name', '')
    version = st.text_input('Version', '')

    st.markdown('### Azure Configuration Inputs')

    resourcegroup = st.text_input('Resource group name', '')
    resourcegroup_createnew = st.checkbox(
        'Create new', key='resourcegroup_createnew')

    acrname = st.text_input('Container registry name', '')
    acr_createnew = st.checkbox('Create new', key='acr_createnew')

    aksname = st.text_input('Kubernetes cluster name', '')
    aks_createnew = st.checkbox('Create new', key='aks_createnew')
    if aks_createnew:
        node_number = st.text_input('Number of nodes', '')
        # replica_number = st.text_input('Number of replicas', '')

    if st.button('Deploy'):
        my_bar = st.progress(0)
        placeholder = st.empty()
        placeholder2 = st.empty()

        if resourcegroup_createnew:
            with placeholder.beta_container():
                st.write('Creating Resource Group')
            run_command('az group create --name ' +
                        resourcegroup + ' --location eastus')
            with placeholder.beta_container():
                st.write('Resource Group created')
        my_bar.progress(10)

        # ACR creation and login
        if acr_createnew:
            with placeholder.beta_container():
                st.write('Creating Container Registry')
            run_command(
                'az acr create --resource-group ' + resourcegroup + ' --name ' + acrname + ' --sku Basic')
            with placeholder.beta_container():
                st.write('Container Registry created')
        run_command('az acr login --name ' + acrname)
        with placeholder.beta_container():
            st.write('Successfully logged into Container Registry')
        my_bar.progress(20)

        # Docker image handling
        with placeholder.beta_container():
            st.write('Tagging docker image')
        run_command('docker tag ' + docker_image + ' ' +
                    acrname + '.azurecr.io/'+docker_image+':' + version)
        with placeholder.beta_container():
            st.write('Docker image tagged')

        my_bar.progress(40)
        with placeholder.beta_container():
            st.write('Pushing docker image to Container Registry')
        run_command('docker push '+acrname+'.azurecr.io/' +
                    docker_image+':' + version)
        with placeholder.beta_container():
            st.write('Docker image pushed to Container Registry')
        my_bar.progress(50)

        # AKS creation and login
        if aks_createnew:
            with placeholder.beta_container():
                st.write('Creating Kubernetes Service')
            run_command('az aks create' +
                        ' --resource-group ' + resourcegroup +
                        ' --name ' + aksname +
                        ' --node-count ' + node_number +
                        ' --generate-ssh-keys' +
                        ' --attach-acr ' + acrname)
        my_bar.progress(60)
        with placeholder.beta_container():
            st.write('Kubernetes service created')

        run_command(
            'az aks get-credentials --resource-group ' + resourcegroup+' --name ' + aksname)
        my_bar.progress(70)
        with placeholder.beta_container():
            st.write('Logged into Kubernetes Service')

        # Generate the yaml file
        my_bar.progress(80)
        generate_yaml(dep_name, acrname, version, docker_image)
        with placeholder.beta_container():
            st.write('Kubernetes configuration file generated')

        with placeholder.beta_container():
            st.write('Deploying Kubernetes...')
        run_command('kubectl apply -f utils/' + dep_name + '.yaml')
        my_bar.progress(90)
        with placeholder.beta_container():
            st.write('Kubernetes deployed')
        my_bar.progress(100)

with st.beta_expander("Check deployment status"):
    dep_name2 = st.text_input('Deployment name (Can be same as above)', '')
    if st.button('Get public IP'):
        placeholder4 = st.empty()
        run_command_getip('kubectl get service '+dep_name2)
