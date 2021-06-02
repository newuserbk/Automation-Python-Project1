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
                    bat "npm cache clean --force"
                    echo "npm cache cleaned......."
                    bat "npm config set registry https://github.com/newuserbk/Automation-Python-Project1"
                    bat "npm install -g newman"
                    echo "newman installed globally......"
                    root = pwd()
                    echo "Root Directory is : "+root
                    dir("${root}/APIPostmanCollections"){
                        bat 'ls -al'
                        echo "Listing all directories as below :"
                        bat "newman run test_Collection.postman_collection.json --insecure"
                    }
                }
            }
            catch (Exception ex)
            {
                echo "stage failed, but we continue : "+ex
            }
       }
    //}
}