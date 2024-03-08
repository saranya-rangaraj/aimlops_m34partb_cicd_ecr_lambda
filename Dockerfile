FROM public.ecr.aws/lambda/python:3.11

# Copy application files
ADD /iris_model_lambda/* ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "iris_lambda_function.handler" ]

