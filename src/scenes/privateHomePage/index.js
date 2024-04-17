import React from "react";
import Navbar from "../navbar";
import DragAndDrop from "../../components/DragAndDrop";

const PrivateHomePage = () => {
  return (
    <>
      <Navbar />
      <div class="px-40 pb-16">
        <div class="py-10 mr-60">
          <span class="text-black text-5xl font-bold">
            Jednoducho prehliadaj registre právnických osôb v oblasti umenia,
            kultúry a kreatívneho priemyslu
          </span>
        </div>
        <hr class="h-px bg-gray-200 border-0 dark:bg-gray-700"></hr>
        <div class="text-3xl pt-4 font-bold text-blue-600">
          Hľadanie Subjektov
        </div>
        <div class="font-bold py-4">Aké subjekty chcete zobraziť?</div>
        <div class="pb-8">
          <div class="flex flex-row justify-between">
            <form class="flex flex-col md:flex-row gap-3 ">
              <div class="flex">
                <input
                  type="text"
                  placeholder="Zadajte IČO"
                  class="w-full md:w-80 px-3 h-10 rounded-l border-2 border-blue-600 focus:outline-none focus:border-blue-600"
                />
                <button
                  type="submit"
                  class="bg-blue-600 hover:bg-blue-650 text-white rounded-r px-2 md:px-3 py-0 md:py-1"
                >
                  hľadaj
                </button>
              </div>
              <select
                id="pricingType"
                name="pricingType"
                class="w-30 h-10 border-2 border-blue-600 focus:outline-none focus:border-blue-650 text-blue-600 rounded px-2 md:px-3 py-0 md:py-1 tracking-wider"
              >
                <option value="All" selected="">
                  Všetky
                </option>
                <option value="Freemium">Galérie</option>
                <option value="Free">Divadlá</option>
                <option value="Paid">Múzeá</option>
              </select>
            </form>
            <div class="flex gap-3">
              <button class="bg-green-600 hover:bg-blue-650 text-white font-bold py-2 px-4 rounded inline-flex items-center">
                <svg
                  class="fill-current w-4 h-4 mr-2"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 20 20"
                >
                  <path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z" />
                </svg>
                <span>stiahnuť</span>
              </button>
              <select
                id="pricingType"
                name="pricingType"
                class="w-30 h-10 border-2 border-blue-600 focus:outline-none focus:border-blue-600 text-blue-600 rounded px-2 md:px-3 py-0 md:py-1 tracking-wider"
              >
                <option value="All" selected="">
                  XLSX
                </option>
                <option value="Freemium">CSV</option>
              </select>
            </div>
          </div>
        </div>

        <hr class="h-px bg-gray-200 border-0 dark:bg-gray-700"></hr>

        <div class="text-3xl pt-4 font-bold text-blue-600">
          Pridávanie Subjektov
        </div>

        <div class="py-8 w-screen">
          <DragAndDrop />
        </div>
      </div>
    </>
  );
};

export default PrivateHomePage;
