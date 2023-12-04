import kopf
import logging
import os
import shutil
import uuid

DEFAULT_PATH = "/home/gntouts/kopferator"


def generate_random_filename():
    # Generate a random UUID and use it as part of the file name
    random_uuid = str(uuid.uuid4())
    filename = f'{random_uuid}.txt'
    return filename


@kopf.on.create('filemanagers')
def create_fn(body, **kwargs):
    desiredFileCount = int(body['spec']['files'])
    name = body['metadata']['name']
    namespace = body['metadata']['namespace']

    logging.info(
        f'A create handler is called for "{name}" in namespace "{namespace}" for {desiredFileCount} files.')
    targetDir = os.path.join(DEFAULT_PATH, namespace)
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)
        logging.info(f"Directory '{targetDir}' created.")
    else:
        logging.info(f"Directory '{targetDir}' already exists.")

    existing_files = os.listdir(targetDir)

    if len(existing_files) == desiredFileCount:
        logging.info("Resources already exist.")
        return
    if len(existing_files) < desiredFileCount:
        logging.info("Creating extra files.")
        amount = desiredFileCount - len(existing_files)
        for i in range(amount):
            temp = os.path.join(targetDir, generate_random_filename())
            with open(temp, 'w') as file:
                file.write(f'This is file {i}')
        return
    logging.info("Deleting extra files.")
    amount = len(existing_files) - desiredFileCount
    for i in range(amount):
        temp = os.path.join(targetDir, existing_files[i])
        os.remove(temp)
        logging.info


@kopf.on.update('filemanagers')
def update_fn(body, **kwargs):
    desiredFileCount = int(body['spec']['files'])
    name = body['metadata']['name']
    namespace = body['metadata']['namespace']

    logging.info(
        f'An update handler is called for "{name}" in namespace "{namespace}" for {desiredFileCount} files.')
    targetDir = os.path.join(DEFAULT_PATH, namespace)
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)
        logging.info(f"Directory '{targetDir}' created.")
    else:
        logging.info(f"Directory '{targetDir}' already exists.")

    existing_files = os.listdir(targetDir)

    if len(existing_files) == desiredFileCount:
        logging.info("Resources already exist.")
        return
    if len(existing_files) < desiredFileCount:
        logging.info("Creating extra files.")
        amount = desiredFileCount - len(existing_files)
        for i in range(amount):
            temp = os.path.join(targetDir, generate_random_filename())
            with open(temp, 'w') as file:
                file.write(f'This is file {i}')
        return
    logging.info("Deleting extra files.")
    amount = len(existing_files) - desiredFileCount
    for i in range(amount):
        temp = os.path.join(targetDir, existing_files[i])
        os.remove(temp)
        logging.info
    return


@kopf.on.delete('filemanagers')
def delete_fn(body, **kwargs):
    desiredFileCount = int(body['spec']['files'])
    name = body['metadata']['name']
    namespace = body['metadata']['namespace']

    logging.info(
        f'A delete handler is called for "{name}" in namespace "{namespace}" for {desiredFileCount} files.')
    targetDir = os.path.join(DEFAULT_PATH, namespace)
    if os.path.exists(targetDir):
        shutil.rmtree(targetDir)

@kopf.timer('filemanagers', interval=10.0)
def ensure_fn(spec, body, **kwargs):
    name = body['metadata']['name']
    namespace = body['metadata']['namespace']
    desiredFileCount = int(spec['files'])
    logging.info(
        f'A timer handler is called for "{name}" in namespace "{namespace}" for {desiredFileCount} files.')
    targetDir = os.path.join(DEFAULT_PATH, namespace)
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)
        logging.info(f"Directory '{targetDir}' created.")
    else:
        logging.info(f"Directory '{targetDir}' already exists.")

    existing_files = os.listdir(targetDir)

    if len(existing_files) == desiredFileCount:
        logging.info("Resources already exist.")
        return
    if len(existing_files) < desiredFileCount:
        logging.info("Creating extra files.")
        amount = desiredFileCount - len(existing_files)
        for i in range(amount):
            temp = os.path.join(targetDir, generate_random_filename())
            with open(temp, 'w') as file:
                file.write(f'This is file {i}')
        return
    logging.info("Deleting extra files.")
    amount = len(existing_files) - desiredFileCount
    for i in range(amount):
        temp = os.path.join(targetDir, existing_files[i])
        os.remove(temp)
        logging.info
    return