import React from "react";
import slovensko from "../../assets/img/slovensko.svg";

const Navbar = () => {
  return (
    <div>
      <nav className="flex justify-between items-center bg-blue-950 py-3 px-40">
        <div className="flex items-center">
          <button className="text-white font-bold text-l hover:underline">
            Oficiálna stránka verejnej správy SR
          </button>
        </div>
        <div className="flex space-x-8">
          <button className="text-white text-l hover:underline">
            Slovenčina
          </button>
        </div>
      </nav>
      <nav className="flex justify-between items-center bg-white border-b-2 border-black-1 shadow-md py-4 px-40">
        <div className="flex items-center">
          <img src={slovensko} alt="Logo" className="h-20 mr-4" />
          <span className="text-blue-950 font-bold text-3xl">
            Kulturne registre
          </span>
        </div>
        <div className="flex space-x-8">
          <button className="text-blue-950 text-xl">API</button>
          <button className="text-blue-950 text-xl">Historia</button>
          <button className="text-blue-950 text-xl">Ziadosti</button>
          <button className="text-blue-950 text-xl">Odhlasit sa</button>
        </div>
      </nav>
    </div>
  );
};

export default Navbar;
