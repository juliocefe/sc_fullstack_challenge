import 'vite/modulepreload-polyfill';
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import AutContext from "./Context";
import "@fontsource/roboto/300.css";
import "@fontsource/roboto/400.css";
import "@fontsource/roboto/500.css";
import "@fontsource/roboto/700.css";
import "./index.css"

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <AutContext.Provider>
      <App />
    </AutContext.Provider>
  </React.StrictMode>
);
