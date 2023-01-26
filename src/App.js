import logo from './images/logo.png';
import './css/App.scss';
import React from 'react'

function App() {

    const [data, setData] = React.useState([{}]);
    
    React.useEffect(() => {
        fetch("/books").then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                console.log(data)
            }
        )
    }, []);

    return (
        <div className="App">
            <div className='logo-wrapper'>
                <img className='logo' src={logo}></img>
            </div>
            {(typeof data.book === 'undefined') ? (
                <p>Loading...</p>
            ) : (
                <p>{data.book}</p>
            )}
        </div>
    );
}

export default App;
