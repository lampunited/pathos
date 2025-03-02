import React, { useState } from 'react';
import './index.css';

function App() {
  const [searchInput, setSearchInput] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!searchInput.trim()) {
      setError('Please enter a query');
      return;
    }
    setLoading(true);
    setError('');
    setResults([]);
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
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      className="
        min-h-screen
        flex flex-col
        bg-gradient-to-b
        from-[#1f1f2e]
        via-[#1f1f2e]
        to-[#4e4376]
        text-white
        leading-normal
        tracking-normal
      "
      style={{
        fontFamily: "'Source Sans Pro', sans-serif",
      }}
    >
      {/* NAVBAR */}
      <nav className="w-full py-5 absolute">
        <div className="container mx-auto px-6 md:px-12 flex items-center justify-between">
          {/* Brand / Logo */}
          <div className="text-lg font-bold text-gray-100">
            <a href="#" className="flex items-center no-underline hover:no-underline">
              {/* Example logo icon */}
              <svg className="h-8 fill-current inline mr-2" viewBox="0 0 512 512">
                <path d="M256,8C119,8,8,119,8,256s111,248,248,248s248-111,248-248S393,8,256,8z" />
              </svg>
              Rainblur
            </a>
          </div>
          {/* Social Links (optional) */}
          <div className="flex items-center space-x-4">
            <a
              href="#"
              className="text-gray-100 hover:text-gray-300"
              title="Twitter"
            >
              <svg className="h-6 w-6 fill-current" viewBox="0 0 512 512">
                <path d="M459.37,151.716..." />
              </svg>
            </a>
            <a
              href="#"
              className="text-gray-100 hover:text-gray-300"
              title="Facebook"
            >
              <svg className="h-6 w-6 fill-current" viewBox="0 0 512 512">
                <path d="M426.07,86.928..." />
              </svg>
            </a>
          </div>
        </div>
      </nav>

      {/* HERO SECTION */}
      <div className="relative overflow-hidden flex-grow">
        <div className="container mx-auto px-6 md:px-12 relative z-10 flex items-center py-32 xl:py-40">
          <div className="w-full flex flex-col items-center text-center relative z-10">
            <h1 className="font-bold text-5xl text-white leading-tight mt-4">
              Chatbot
            </h1>
            <p className="text-2xl text-gray-200 leading-snug pt-2">
              Ask a Tech Question
            </p>

            {/* Chatbot Form */}
            <form onSubmit={handleSubmit} className="w-full max-w-sm mt-6">
              <div className="flex items-center border-b border-gray-100 py-2">
                <input
                  className="appearance-none bg-transparent border-none w-full text-gray-200 mr-3 py-1 px-2 leading-tight focus:outline-none"
                  type="text"
                  placeholder="Type your question here..."
                  aria-label="Question"
                  value={searchInput}
                  onChange={(e) => setSearchInput(e.target.value)}
                />
                <button
                  className="flex-shrink-0 bg-indigo-700 hover:bg-indigo-800 border-indigo-700 hover:border-indigo-800
                             text-sm border-4 text-white py-1 px-2 rounded"
                  type="submit"
                  disabled={loading}
                >
                  {loading ? 'Searching...' : 'Search'}
                </button>
              </div>
            </form>

            {error && (
              <p className="mt-4 text-center text-red-500">
                Error: {error}
              </p>
            )}
          </div>
        </div>
      </div>

      {/* RESULTS SECTION */}
      <div className="container mx-auto px-6 md:px-12 pb-10">
        {/* Render results if present */}
        {results && results.length > 0 && (
          <div className="bg-white bg-opacity-90 rounded-lg shadow-xl p-6 text-gray-900">
            <h2 className="mb-4 text-xl font-semibold text-gray-900">
              Results
            </h2>
            {results.map((result, index) => (
              <div key={index} className="mb-4 p-4 border-b border-gray-300">
                <p>
                  <strong>Question:</strong> {result.question_text}
                </p>
                {/* Renders answer_text as HTML (dangerouslySetInnerHTML) */}
                <p>
                  <strong>Answer:</strong>{' '}
                  <span
                    dangerouslySetInnerHTML={{ __html: result.answer_text }}
                  />
                </p>
                {/* Distance line removed */}
                <p>
                  <strong>Source:</strong>{' '}
                  <a
                    href={result.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-indigo-600 hover:underline"
                  >
                    {result.url}
                  </a>
                </p>
              </div>
            ))}
          </div>
        )}

        {/* No results found */}
        {results && !loading && results.length === 0 && (
          <p className="mt-4 text-center text-gray-200">
            No results found.
          </p>
        )}
      </div>

      {/* FOOTER */}
      <footer className="w-full py-6 text-center text-gray-200 bg-opacity-50 backdrop-filter backdrop-blur-sm">
        <p>Download our app:</p>
        <div className="flex justify-center space-x-4 mt-2">
          <a href="#" title="Google Play">
            <img
              src="https://upload.wikimedia.org/wikipedia/commons/7/78/Google_Play_Store_badge_EN.svg"
              alt="Google Play"
              className="h-10"
            />
          </a>
          <a href="#" title="App Store">
            <img
              src="https://upload.wikimedia.org/wikipedia/commons/a/ab/Apple-download-badge.svg"
              alt="App Store"
              className="h-10"
            />
          </a>
        </div>
      </footer>
    </div>
  );
}

export default App;
