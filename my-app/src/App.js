import LandingPage from "./pages/LandingPage";
import Description from "./pages/Description";
import About from "./pages/About";

import Register from "./pages/Register";
import Signin2 from "./pages/Signin2";
import { BrowserRouter ,
  Route, Routes,Link} from "react-router-dom";

  

function App() {
  return (
    <>
    <div className="App">
      <header className="App-header">
    <BrowserRouter>
    
      <Routes>
    
        {/* <Route exact path="/" Component={Signin2} />
        <Route  path="/register" Component={Register} /> */}
        <Route  path="/" Component={LandingPage} />
        <Route  path="/description" Component={Description} />
        <Route  path="/about" Component={About} />
        {/* <LandingPage />
        <Description />
        <About />
        <Signin />
        <Register />
        <Signin2 /> */}
     
    </Routes>

    </BrowserRouter>
    </header>
    </div>
    </>
  );
}

export default App;
