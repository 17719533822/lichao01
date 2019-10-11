node('test1'){
    
	stage('Source'){
	    git 'https://github.com/17719533822/lichao01.git'
	}
	
	stage('Build'){
	    parallel(
		//并列任务
		    stage('Build:test1'){
		        steps{
		            echo 'building'
			        sh 'mvn clean install'
				}
			}
        stage('Build:test2'){
		        steps{
		            echo 'building'
			        sh 'mvn clean install'
				}
			}			
		)
	}
	
	stage('Deploy'){
	    steps{
		    sh ''
		}
	}
}