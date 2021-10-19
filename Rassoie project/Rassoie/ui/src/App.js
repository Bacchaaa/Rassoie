import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import Navigation from './components/navbar/navigation';
import {
  BrowserRouter as Router,
  Switch,
  Route
}
from 'react-router-dom';
import Landing from './components/landing/Landing';
import Login from './components/Login';


function App() {
  return (
    <>
      <Router>
        <Navigation />
        <Login />
        <Landing />
      </Router>
    </>
  );
}

export default App;
