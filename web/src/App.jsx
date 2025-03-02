// import Feature from '@components/Feature';
// import Footer from '@components/Footer';
// import logo from '@images/logo.png';

// const features = [
//   {
//     title: 'npm run start',
//     description: 'Run the React app in development mode with live reloading.',
//   },
//   {
//     title: 'npm run build',
//     description: 'Bundles the React app for deployment in production environment.',
//   },
//   {
//     title: 'npm run inline',
//     description: 'Inline all CSS and JS in a single minfied file.',
//   },
// ];

// const App = () => (
//   <div className='flex min-h-screen flex-col justify-center bg-gray-100 py-6 sm:py-12'>
//     <div className='relative py-3 sm:mx-auto sm:max-w-xl'>
//       <div className='to-light-blue-500 absolute inset-0 -skew-y-6 transform bg-gradient-to-r from-cyan-400 shadow-lg sm:-rotate-6 sm:skew-y-0 sm:rounded-3xl' />
//       <div className='relative bg-white px-4 py-10 shadow-lg sm:rounded-3xl sm:p-20'>
//         <div className='mx-auto max-w-md'>
//           <div>
//             <a href='https://digitalinspiration.com/'>
//               <img src={logo} className='h-7 sm:h-8' alt='Logo' />
//             </a>
//           </div>
//           <div className='divide-y divide-gray-200'>
//             <div className='space-y-5 py-8 text-base leading-6 text-gray-700 sm:text-lg sm:leading-7'>
//               <h1 className='text-lg font-semibold text-cyan-600'>
//                 React and Tailwind CSS Starter Kit
//               </h1>
//               <p>Create a React project with Vite and Tailwind CSS.</p>
//               <div className='list-disc space-y-2'>
//                 {features.map((feature) => (
//                   <Feature
//                     key={feature.title}
//                     title={feature.title}
//                     description={feature.description}
//                   />
//                 ))}
//               </div>
//               <p className='text-sm font-medium text-cyan-500'>
//                 Built with Tailwind CSS 4 and React 19.
//               </p>
//             </div>
//             <Footer />
//           </div>
//         </div>
//       </div>
//     </div>
//   </div>
// );

// export default App;

// App.js
import React, { useState } from 'react';
import Footer from '@components/Footer';
import logo from '@images/logo.png';

const App = () => {
  const [searchInput, setSearchInput] = useState('');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResults(null);
    try {
      const response = await fetch('http://127.0.0.1:5000/api/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: searchInput }),
      });
      if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
      }
      const data = await response.json();
      setResults(data);
    } catch (err) {
      setError(err.message);
    }
    setLoading(false);
  };

  return (
    <div className="flex min-h-screen flex-col justify-center bg-[#D9D9D9] py-6 sm:py-12">
      <div className="relative py-3 sm:mx-auto sm:max-w-5xl">
        {/* Background gradient for style */}
        <div className="absolute inset-0 -skew-y-6 transform bg-gradient-to-r from-cyan-400 to-blue-500 shadow-lg sm:-rotate-6 sm:skew-y-0 sm:rounded-3xl" />
        <div className="relative bg-white px-4 py-10 shadow-lg sm:rounded-3xl sm:p-20">
          <div className="mx-auto max-w-md">
            <div className="text-center">
              <h1 className="mt-4 text-5xl font-bold text-[#0077B6]">
                devchotomy
              </h1>
            </div>
            <form onSubmit={handleSubmit} className="mt-6">
              <textarea
                className="w-full rounded-md border border-gray-300 p-2 text-gray-800"
                placeholder="ask a tech question..."
                value={searchInput}
                onChange={(e) => setSearchInput(e.target.value)}
              />
              <button
                type="submit"
                className="mt-4 w-full rounded-md bg-blue-500 py-2 text-white hover:bg-blue-600"
              >
                search
              </button>
            </form>
            {loading && (
              <p className="mt-4 text-center text-gray-600">Loading...</p>
            )}
            {error && (
              <p className="mt-4 text-center text-red-500">Error: {error}</p>
            )}
            {results && Array.isArray(results) && (
              <div className="mt-6">
                <h2 className="mb-2 text-lg font-semibold text-gray-700">Results:</h2>
                <div>
                  {results.map((result, index) => (
                    <div key={index} className="mb-4 rounded-md bg-gray-100 p-4 text-sm text-gray-800">
                      <p><strong>question:</strong> {result.question_text}</p>
                      <p><strong>answer:</strong> {result.answer_text}</p>
                      <p><strong>distance:</strong> {result.distance}</p>
                      <p>
                        <strong>source:</strong>{' '}
                        <a href={result.url} target="_blank" rel="noopener noreferrer">
                          {result.url}
                        </a>
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            )}
            <Footer />
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
