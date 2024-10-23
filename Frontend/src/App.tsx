import React from "react";
import { Route, Routes } from "react-router";
import { Header } from "./Components/Header/Header";
import { routes } from "./Routes/Routes";
import { Footer } from "./Components/Footer/Footer";

export const App = () => {
  return (
    <div>
      <Header />
      <Routes>
        {routes.map((route) => (
          <Route key={route.path} path={route.path} element={<route.component/>} />
        ))}
      </Routes>
      <Footer />
    </div>
  );
};
