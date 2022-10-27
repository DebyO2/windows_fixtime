import os

def RunAsAdmin(path_to_file,*args):
    os.system(r'Powershell -Command "Start-Process "'+path_to_file+'"'+ # CMD running Powershell
                ' -ArgumentList @('+str(args)[1:-1]+')'+ # Arguments. [1:-1] to remove brackets
                ' -Verb RunAs"' # Run file as administrator
    )

RunAsAdmin('fixtime_final.exe','arg1','arg2')