import { useRef, useState } from "react";

export default function DragAndDrop() {
  const [dragActive, setDragActive] = useState(false);
  const inputRef = useRef(null);
  const [files, setFiles] = useState([]);
  function handleChange(e) {
    e.preventDefault();
    console.log("File has been added");
    if (e.target.files && e.target.files[0]) {
      console.log(e.target.files);
      for (let i = 0; i < e.target.files.length; i++) {
        setFiles((prevState) => [...prevState, e.target.files[i]]);
      }
    }
  }

  function handleSubmitFile(e) {
    if (files.length === 0) {
      // no file has been submitted
    } else {
      // write submit logic here
    }
  }

  function handleDrop(e) {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      for (let i = 0; i < e.dataTransfer.files.length; i++) {
        setFiles((prevState) => [...prevState, e.dataTransfer.files[i]]);
      }
    }
  }

  function handleDragLeave(e) {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
  }

  function handleDragOver(e) {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(true);
  }

  function handleDragEnter(e) {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(true);
  }

  function removeFile(fileName, idx) {
    const newArr = [...files];
    newArr.splice(idx, 1);
    setFiles([]);
    setFiles(newArr);
  }

  function openFileExplorer() {
    inputRef.current.value = "";
    inputRef.current.click();
  }

  return (
    <div className="flex items-center justify-left">
      <form
        className={`border-dashed border-gray-300 border-2 ${
          dragActive ? "bg-stone-100" : "bg-white"
        }  p-4 w-1/3 rounded-lg  min-h-[10rem] text-center flex flex-col items-center justify-center`}
        onDragEnter={handleDragEnter}
        onSubmit={(e) => e.preventDefault()}
        onDrop={handleDrop}
        onDragLeave={handleDragLeave}
        onDragOver={handleDragOver}
      >
        {/* this input element allows us to select files for upload. We make it hidden so we can activate it when the user clicks select files */}
        <input
          placeholder="fileInput"
          className="hidden"
          ref={inputRef}
          type="file"
          multiple={true}
          onChange={handleChange}
          accept=".xlsx,.xls,.csv,.pdf"
        />

        <p>
          Preneste súbory sem
          <p>
            alebo{" "}
            <span
              className="font-bold text-blue-600 cursor-pointer"
              onClick={openFileExplorer}
            >
              <u>Zvoľte Súbory</u>
            </span>{" "}
            a nahrajte ich
          </p>
          <p class="text-gray-400">
            (Podporované formáty: .xlsx, .xls, .csv, .pdf)
          </p>
        </p>

        <div className="flex flex-col items-center p-3">
          {files.map((file, idx) => (
            <div key={idx} className="flex flex-row space-x-5">
              <span>{file.name}</span>
              <span
                className="text-red-500 cursor-pointer"
                onClick={() => removeFile(file.name, idx)}
              >
                remove
              </span>
            </div>
          ))}
        </div>

        <button
          className="bg-green-600 rounded-lg p-2 mt-3 w-auto"
          onClick={handleSubmitFile}
        >
          <span className="p-2 text-white font-bold">Submit</span>
        </button>
      </form>
    </div>
  );
}
