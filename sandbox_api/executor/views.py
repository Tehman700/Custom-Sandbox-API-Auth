import os
import uuid
import subprocess
import time
import tempfile

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CodeExecutionSerializer

class CodeExecutionView(APIView):
    def post(self, request):
        serializer = CodeExecutionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data['code']
        input_data = serializer.validated_data.get('input', '')
        language = serializer.validated_data['language']

        # Save code to a temp file
        uid = str(uuid.uuid4())
        

        temp_dir = tempfile.gettempdir()  # This works cross-platform

        code_filename = os.path.join(temp_dir, f"{uid}.py")
        input_filename = os.path.join(temp_dir, f"{uid}_input.txt")


        with open(code_filename, 'w') as f:
            f.write(code)

        with open(input_filename, 'w') as f:
            f.write(input_data)

        # Run Docker command
        docker_command = [
            "docker", "run", "--rm",
            "-v", f"{code_filename}:/app/code.py",
            "-v", f"{input_filename}:/app/input.txt",
            "--network=none",
            "--memory=128m",
            "--cpus=0.5",
            "python-sandbox-image"
        ]

        try:
            start_time = time.time()
            result = subprocess.run(
                docker_command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5
            )
            end_time = time.time()

            stdout = result.stdout.decode()
            stderr = result.stderr.decode()
            exit_code = result.returncode
            exec_time = round(end_time - start_time, 3)

            verdict = "Accepted" if exit_code == 0 else "Runtime Error"
            if exec_time > 2.0:
                verdict = "Time Limit Exceeded"

        except subprocess.TimeoutExpired:
            stdout = ""
            stderr = "Execution timed out"
            exit_code = -1
            exec_time = 2.001
            verdict = "Time Limit Exceeded"

        # Cleanup
        os.remove(code_filename)
        os.remove(input_filename)

        return Response({
            "stdout": stdout,
            "stderr": stderr,
            "exit_code": exit_code,
            "time": exec_time,
            "verdict": verdict
        })
