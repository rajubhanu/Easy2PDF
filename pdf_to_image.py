
def convert(file_path):
    output_path = file_path.replace('.pdf', '.png')
    with open(file_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
        f_out.write(f_in.read())
    return output_path
