import React from 'react'
import FileForm from './fileform'

const App = () => {
  // const [message, setMessage] = useState("");
  // const getMessage = async()=>{
  //   const requestOptions = {
  //     method: "POST",
  //     headers: {
  //       "Content-Type": "multipart/form-data",
  //     },
  //   };
  //   const response = await fetch("/predict", requestOptions);
  //   const data = await response.json();

  //   if(!response.ok){
  //     console.log("oops something went wrong");
  //   }
  //   else{
  //     setMessage(data.message);
  //   }
  // };

  // useEffect(()=>{
  //   getMessage();
  // }, []);

  return (
    <div>
      <FileForm/>
    </div>
  )
}

export default App
