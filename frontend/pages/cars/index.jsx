import React from "react";
import axios from "axios";
import Link from "next/link";

function Cars({ data }) {
  return (
    <div className="top-20 w-screen">
      <h1 className="block text-gray-700 text-lg font-bold mb-2">
        List of cars
      </h1>
      <ul className="px-8 pt-6 pb-8 mb-4">
        {data.map((car) => (
          <li key={car._id}>
            <Link href={`/cars/${car._id}`}>{car.model}</Link> </li>
        ))}
      </ul>
    </div>
  );
}

export default Cars;

export async function getServerSideProps() {
  const { data } = await axios.get("http://127.0.0.1:8000/api/v1/");
  return { props: { data } };
}
