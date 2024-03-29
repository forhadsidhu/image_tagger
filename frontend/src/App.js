import React, { useEffect } from "react";
import { createGlobalStyle } from "styled-components";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import Home from "./pages/home";
import Login from './pages/auth';
import ImagePage from "./pages/gallery";
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


import { auth } from './firebase';
import {useDispatch} from 'react-redux';

const GlobalStyle = createGlobalStyle`

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: ubuntu;
}

`;

function App() {
  const dispatch = useDispatch();

  // to check firebase auth state
  useEffect(() => {
    const unsubscribe = auth.onAuthStateChanged(async (user) => {
      if (user) {
        const idTokenResult = await user.getIdTokenResult()
        console.log('user', user)
        dispatch({
          type: 'LOGGED_IN_USER',
          payload: {
            email: user.email,
            token: idTokenResult.token
          }
        })
      }

    })
    return () => unsubscribe();
  }, [])

  return (
    <>
      <GlobalStyle />
      <ToastContainer />
      <BrowserRouter >
        <Switch>
          <Route path="/" component={Home} exact />
          <Route  path="/login" component={Login} />
          <Route path="/image_world" component={ImagePage}/>
        </Switch>
      </BrowserRouter >
    </>
  );
}

export default App;
