import React, { useState } from 'react';
import './index.css';

function App() {
  const [searchInput, setSearchInput] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    document.body.classList.add('gradient');
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
        text-white
        leading-normal
        tracking-normal
      "
      style={{
        fontFamily: "'Source Sans Pro', sans-serif",
      }}
    >
      <nav className="w-full py-5 absolute">
        <div className="container mx-auto px-6 md:px-12 flex items-center justify-end">
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

      <div className="relative overflow-hidden flex-grow">
        <div className="container mx-auto px-6 md:px-12 relative z-10 flex items-center py-32 xl:py-40">
          <div className="w-full flex flex-col items-center text-center relative z-10">
            <h1 className="font-bold text-5xl text-white leading-tight mt-4">
              pathos
            </h1>
            <p className="text-2xl text-gray-200 leading-snug pt-2">
              tech questions with human responses
            </p>
            <form onSubmit={handleSubmit} className="w-full max-w-sm mt-6">
              <div className="flex items-center py-2">
                <input
                  className="
                    appearance-none
                    bg-transparent
                    border-none
                    w-full
                    text-gray-200
                    mr-3
                    py-1
                    px-2
                    leading-tight
                    outline-none
                    focus:outline-none
                    focus:ring-0
                  "
                  type="text"
                  placeholder="your question..."
                  aria-label="Question"
                  value={searchInput}
                  onChange={(e) => setSearchInput(e.target.value)}
                />
                <button
                  className="
                    flex-shrink-0
                    text-sm
                    text-white
                    py-1
                    px-2
                    rounded
                    border-2
                    border-indigo-700
                    bg-transparent
                    hover:bg-transparent
                    transition-colors
                  "
                  type="submit"
                  disabled={loading}
                >
                  {loading ? 'searching...' : 'search'}
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

      <div className="container mx-auto px-6 md:px-12 pb-10">
        {results && results.length > 0 && (
          <div className="bg-white/60 rounded-lg shadow-xl p-6 text-gray-900">
            <h2 className="mb-4 text-xl font-semibold text-gray-900">
              Results
            </h2>
            {results.map((result, index) => {
              const logoSrc = getLogoSrc(result.url);
              return (
                <div
                  key={index}
                  className="flex items-start mb-4 p-4 border-b border-gray-300"
                >
                  <img
                    src={logoSrc}
                    alt="Logo"
                    className="w-10 h-10 mr-4"
                  />
                  <div>
                    <div
                      className="text-gray-900"
                      dangerouslySetInnerHTML={{ __html: result.answer_text }}
                    />
                    <p className="mt-2">
                      <strong>From:</strong>{" "}
                      <a
                        href={result.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-indigo-600 hover:underline"
                      >
                        {result.question_text}
                      </a>
                    </p>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}

function getLogoSrc(url) {
  if (url.includes("reddit.com")) {
    return "/reddit-icon.png";
  } else if (url.includes("stackoverflow.com")) {
    return "/stack-icon.png";
  }
  return "/default-logo.png";
}

export default App;
