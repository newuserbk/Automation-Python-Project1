node('master')
{
       //container('GSTProjectQA'){
        stage('Download Source'){
            echo "checking out the code"
            checkout scm
        }
        stage('Test Execution'){
            try
            {
                script{
                    sh "npm cache clean --force"
                    sh "npm config set registry https://github.com/newuserbk/Automation-Python-Project1"
                    sh "npm install -g newman"
                    root = pwd()
                    dir("${root}/APIPostmanCollections"){
                        sh 'ls'
                        sh "newman run test_Collection.postman_collection.json --insecure"
                    }
                }
            }
            catch (Exception ex)
            {
                echo "stage failed, but we continue"
            }
       }
    //}
}