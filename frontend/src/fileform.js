import {useState} from 'react';
import './fileform.css'

function FileForm(){
    const[file, setFile]=useState(null);
    const[respData, setRespData]=useState("upload a file");

    const handleFileInput = (event) => {
        console.log(event.target)
        setFile(event.target.files[0])
    }

    let resp = {'result':'pls upload file'};
    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append('file', file)
        console.log(formData.get('file'));

        try{
            const endpoint = "http://127.0.0.1:8000/predict"
            const response = await fetch(endpoint, {
                method: "POST",
                body: formData
            }).catch(console.error);
            resp = await response.json()
            setRespData(resp['result'])
            console.log(resp['result'])
            

            if(response.ok){
                console.log("file uploaded")
                
            }
            else{
                console.log("failed to upload")
            }
            

        }
        catch(error){
            console.error(error);
        }
        
    }

    return(
        <div style={{backgroundColor: '#F6F5F5'}}>
            <h1 style={{textAlign: 'center', fontFamily: 'sans-serif'}}>Voice Based Sentiment Analysis</h1>
            <form onSubmit={handleSubmit}>
                <input type='file' onChange={handleFileInput} className='aud'/><br/>
                <button type='submit' className='sub'>Submit</button>
            </form>

            {file && <p>{file.name}</p>}
            <h1 style={{fontFamily: 'sans-serif'}}>Response is: </h1>
            <h2 style={{fontFamily: 'sans-serif'}}>{respData}</h2>
            
        </div>
    )
}

export default FileForm