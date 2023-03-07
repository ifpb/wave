import sys
import subprocess
import os

class Provision:
    def __init__(self, script_dir: str):
        self.__script_dir = script_dir 

    def get_script_dir(self):
        return self.__script_dir

    def set_script_dir(self, setPath):
        self.__script_dir = setPath
    
    def execute_command(self, command):
        # script_dir = os.path.dirname(os.path.realpath(__file__))
        # os.chdir(script_dir)
        try:
            result = subprocess.run(f"cd {self.get_script_dir()}; {command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return e.stderr.decode()

    def up(self):
        command = "vagrant up"
        # status_cmd = "vagrant status | grep -Eow 'running' | head -n1"
        # status = self.execute_command(status_cmd)
        # if(status == 'running'):
        #     self.reload_env()
        return self.execute_command(command)

    
    # def reload_env(self):
    #     command = "vagrant reload"
    #     return self.execute_command(command)

    def down(self):
        command = "vagrant destroy -f"
        return self.execute_command(command)

   
    def execute_scenario(self, duration):
        command = f"vagrant ssh client -c 'iperf -c server -t {duration} > /vagrant/result.json'"
        return self.execute_command(command)

    def result(self):
        command = "vagrant ssh client -c 'cat /vagrant/result.json'"
        return self.execute_command(command)