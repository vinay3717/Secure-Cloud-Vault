# Single-Node Hadoop HDFS Setup on WSL2 (Ubuntu)

This document describes the exact setup steps and configuration used for the Hadoop Distributed File System (HDFS) running on WSL2 Ubuntu for Project #9 (**Private LAN SaaS Cloud Storage over HDFS**).

---

## 1. Environment & Prerequisites

- **OS**: Windows 11 with WSL2 (Ubuntu 26.04 LTS)
- **Java**: OpenJDK 11 (`/usr/lib/jvm/java-11-openjdk-amd64`)
- **Hadoop**: Apache Hadoop 3.3.6 (installed at `/usr/local/hadoop`)
- **HDFS Port**: `hdfs://localhost:9000`
- **WebHDFS Port**: `http://localhost:9870`
- **Base Storage Path**: `/saas_cloud`

---

## 2. Step-by-Step Installation

### Step 2.1 — Package Installation
Inside WSL Ubuntu, installed Java 11, OpenSSH server, and Python tooling:
```bash
sudo apt update
sudo apt install -y openjdk-11-jdk ssh openssh-server rsync python3-pip python3-venv wget curl
```

### Step 2.2 — Passwordless SSH Configuration
Hadoop cluster scripts require passwordless SSH access even on single-node localhost:
```bash
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
ssh -o StrictHostKeyChecking=no localhost
```

### Step 2.3 — Hadoop 3.3.6 Download & Extraction
```bash
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz -O /tmp/hadoop-3.3.6.tar.gz
sudo tar -xzf /tmp/hadoop-3.3.6.tar.gz -C /usr/local/
sudo ln -sfn /usr/local/hadoop-3.3.6 /usr/local/hadoop
sudo chown -R $USER:$USER /usr/local/hadoop-3.3.6 /usr/local/hadoop
```

### Step 2.4 — Environment Variables
Added to `~/.bashrc`:
```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
```
And set `export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64` in `/usr/local/hadoop/etc/hadoop/hadoop-env.sh`.

---

## 3. Configuration Files

### `core-site.xml` (`/usr/local/hadoop/etc/hadoop/core-site.xml`)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

### `hdfs-site.xml` (`/usr/local/hadoop/etc/hadoop/hdfs-site.xml`)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.webhdfs.enabled</name>
        <value>true</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:///home/vinay_umesh_gole/hadoop_data/hdfs/namenode</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:///home/vinay_umesh_gole/hadoop_data/hdfs/datanode</value>
    </property>
    <property>
        <name>dfs.permissions.enabled</name>
        <value>false</value>
    </property>
</configuration>
```

---

## 4. NameNode Formatting and Startup

Formatted the NameNode (run once only):
```bash
hdfs namenode -format -force
```

Created systemd service `/etc/systemd/system/hadoop-hdfs.service` so Hadoop daemons persist reliably across WSL sessions:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now hadoop-hdfs.service
```

Verified all three daemons are running with `jps`:
- `NameNode`
- `DataNode`
- `SecondaryNameNode`

Created base directory for SaaS app:
```bash
hdfs dfs -mkdir -p /saas_cloud
hdfs dfs -chmod 777 /saas_cloud
```

---

## 5. WebHDFS Verification

Checked WebHDFS HTTP endpoint:
```bash
curl -sI http://localhost:9870
```
Verified Python `hdfs.InsecureClient` connection, chunk write, and readback tests pass.
