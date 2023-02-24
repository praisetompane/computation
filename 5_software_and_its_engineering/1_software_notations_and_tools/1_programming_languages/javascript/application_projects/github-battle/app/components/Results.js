let React = require('react')
let Api = require('../utils/api')
let queryString = require('query-string')
let Link = require('react-router-dom').Link
let PropTypes = require('prop-types')
let PlayerPreview = require('./PlayerPreview')
let Loading = require('./Loading')

function Profile(props) {
    let info = props.info

    return (
        <PlayerPreview avatar={info.avatar_url} username={info.login}>
            <ul className='space-list-items'>
                {info.name && <li>{info.name}</li>}
                {info.location && <li>{info.location}</li>}
                {info.company && <li>{info.company}</li>}
                <li>Followers: {info.followers}</li>
                <li>Following: {info.following}</li>
                <li>Public Repos: {info.public_repos}</li>
                {info.blog && <li><a href={info.blog}></a></li>}
            </ul>
        </PlayerPreview>
    )
}

Profile.propTypes = {
    info: PropTypes.object.isRequired
}

function Player(props) {
    return (
        <div>
            <h1 className='header'>{props.label}</h1>
            <h3 style={{ textAlign: 'center' }}>Score: {props.score}</h3>
            <Profile info={props.profile} />
        </div>
    )
}

Player.propTypes = {
    label: PropTypes.string.isRequired,
    score: PropTypes.number.isRequired,
    profile: PropTypes.object.isRequired
}
class Results extends React.Component {

    constructor(props) {
        super(props)

        this.state = {
            winner: null,
            loser: null,
            error: null,
            loading: true
        }
    }

    componentDidMount() {
        let players = queryString.parse(this.props.location.search)
        Api.battle([
            players.playerOneName,
            players.playerTwoName
        ]).then((results) => {
            if (results === null) {
                return this.setState(() => {
                    return {
                        error: 'Looks like there was an error. Check that bot users existon GitHub',
                        loading: false
                    }
                })
            }
            this.setState(() => {
                return {
                    winner: results[0],
                    loser: results[1],
                    error: null,
                    loading: false
                }
            })
        })
    }

    render() {
        let error = this.state.error
        let winner = this.state.winner
        let loser = this.state.loser
        let loading = this.state.loading

        if (loading) {
            return <Loading />
        }

        if (error) {
            return (
                <div>
                    <p>{error}</p>
                    <Link to='/battle'> Reset </Link>
                </div>
            )
        }

        return (
            <div className='row'>
                <Player
                    label='Winner'
                    score={winner.score}
                    profile={winner.profile}
                />

                <Player
                    label='Loser'
                    score={loser.score}
                    profile={loser.profile}
                />
            </div>
        )
    }
}

module.exports = Results