FROM ubuntu:20.04

# Set non-interactive mode to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install tzdata and configure timezone to avoid interactive prompts
RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -fs /usr/share/zoneinfo/UTC /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata

# Install other required packages
RUN apt-get install -y wget unzip python3 python3-pip openjdk-11-jdk

# Install Gradle
RUN wget --no-check-certificate https://services.gradle.org/distributions/gradle-7.0-bin.zip \
    && unzip gradle-7.0-bin.zip -d /opt/ \
    && ln -s /opt/gradle-7.0/bin/gradle /usr/bin/gradle

# Install Allure
RUN wget --no-check-certificate https://github.com/allure-framework/allure2/releases/download/2.13.8/allure-2.13.8.zip \
    && unzip allure-2.13.8.zip -d /opt/ \
    && ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose port 8000
EXPOSE 8080

# Default command to build the project, run tests, generate the Allure report, and serve it
CMD ["sh", "-c", "gradle build && pytest --alluredir=./allure-results && allure generate allure-results --clean -o allure-report && python3 -m http.server 8000 --directory /app/allure-report"]
